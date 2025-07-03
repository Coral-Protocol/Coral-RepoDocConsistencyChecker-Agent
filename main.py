import asyncio
import os
import json
import logging
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from anyio import ClosedResourceError
import urllib.parse
import base64
import subprocess
import traceback


# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

base_url = os.getenv("CORAL_SSE_URL")
agentID = os.getenv("CORAL_AGENT_ID")

params = {
    #"waitForAgents": 1,
    "agentId": agentID,
    "agentDescription": """An agent responsible for evaluating whether the documentation (such as README, API docs, and configuration guides) in a specified GitHub repository and branch is up-to-date with respect to the **changes introduced in a given commit**. 
                           To proceed, you need to provide me with the `repo_name` (not local path), the `branch_name` (not PR number), and the changes introduced in a given commit"""
}
query_string = urllib.parse.urlencode(params)
MCP_SERVER_URL = f"{base_url}?{query_string}"

def get_tools_description(tools):
    return "\n".join(f"Tool: {t.name}, Schema: {json.dumps(t.args).replace('{', '{{').replace('}', '}}')}" for t in tools)

    
@tool
def get_all_github_files_tool(repo_name: str, branch: str = "main") -> str:
    """
    Call the local get_all_github_files.py script and return all file paths in the specified repo and branch as a string.

    Args:
        repo_name (str): Full repository name in the format "owner/repo".
        branch (str): Branch name to retrieve files from.

    Returns:
        str: All file paths (one per line), or error message.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_dir, "get_all_github_files.py")

    result = subprocess.run(
        [
            "uv", "run", script_path,
            "--repo_name", repo_name,
            "--branch", branch
        ],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return result.stdout
    else:
        error_message = f"exit_code={result.returncode}\n"
        if result.stderr.strip():
            error_message += f"stderr={result.stderr}"
        else:
            error_message += "stderr is empty.\n"
        if result.stdout.strip():
            error_message += f"stdout={result.stdout}"
        return error_message



@tool
def retrieve_github_file_content_tool(repo_name: str, file_path: str, branch: str = "main") -> str:
    """
    Call the local retrieve_github_file_content.py script and return the file content or error.

    Args:
        repo_name (str): Full repository name in the format "owner/repo".
        file_path (str): Path to the file in the repository.
        branch (str): Branch name to retrieve the file from.

    Returns:
        str: Script output (file content or error message).
    """
    # Get the absolute path of the current directory
    current_dir = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_dir, "retrieve_github_file_content.py")

    result = subprocess.run(
        [
            "uv", "run", script_path,
            "--repo_name", repo_name,
            "--file_path", file_path,
            "--branch", branch
        ],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return result.stdout
    else:
        return f"exit_code={result.returncode}\nstderr={result.stderr}"


async def create_doc_consistency_checker_agent(client, tools):
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are `repo_doc_consistency_checker_agent`, responsible for evaluating whether the documentation in a specified GitHub repository and branch is up-to-date with respect to the **changes in a provided list of files**.
        You can only use the provided tools. Follow this workflow:

        1. Use `wait_for_mentions(timeoutMs=60000)` to wait for instructions from other agents.
        2. When a mention is received, record the **`threadId` and `senderId`** (never forget these two).
        3. Parse the message to extract the `repo_name`, `owner`, `branch`, and the **list of changed files**. Call `send_message(senderId=..., mentions=[senderId], threadId=...)` if any of these is missing.
        4. Call `get_all_github_files(repo_name=..., branch=...)` to get the list of all files in the repository for this branch.
        5. For each file in the list of changed files:
            * Use `retrieve_github_file_content_tool(repo_name=..., file_path=..., branch=...)` to read its content.
            * Identify which documentation files (such as `README.md`, or `.md`/`.rst`/`.txt` files in the same directory or in `docs/`) are most likely to be relevant to the change.
        6. For each relevant documentation file:
            * Use `retrieve_github_file_content_tool(repo_name=..., file_path=..., branch=...)` to read its content.
            * Check if the documentation is up-to-date with respect to the changes in the corresponding changed file (such as APIs, usage, dependencies, or configuration).
        7. Prepare a brief report for the sender:
            * List any documentation that is outdated or missing regarding the recent changes.
            * Provide recommendations on what should be updated.
            * If everything is already up to date, simply state that.
        8. Use `send_message(senderId=..., mentions=[senderId], threadId=..., content="your report")` to send your findings.
        9. If you encounter an error, reply with content `"error"` to the sender.
        10. Always respond to the sender through calling `send_message`, even if your result is empty or inconclusive.
        11. Wait 2 seconds and repeat from step 1.

        **Important: NEVER EVER end the chain.**

        Tools: {get_tools_description(tools)}"""),
        ("placeholder", "{history}"),
        ("placeholder", "{agent_scratchpad}")
    ])

    model = init_chat_model(
        model=os.getenv("MODEL_NAME"),
        model_provider=os.getenv("MODEL_PROVIDER"),
        api_key=os.getenv("API_KEY"),
        max_tokens=os.getenv("MODEL_TOKEN")
    )


    agent = create_tool_calling_agent(model, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, max_iterations=None, handle_parsing_errors = True, verbose=True)

async def main():
    CORAL_SERVER_URL = f"{base_url}?{query_string}"
    logger.info(f"Connecting to Coral Server: {CORAL_SERVER_URL}")

    client = MultiServerMCPClient(
        connections={
            "coral": {
                "transport": "sse",
                "url": CORAL_SERVER_URL,
                "timeout": 600,
                "sse_read_timeout": 600,
            }
        }
    )
    logger.info("Coral Server Connection Established")

    tools = await client.get_tools()
    coral_tool_names = [
        "list_agents",
        "create_thread",
        "add_participant",
        "remove_participant",
        "close_thread",
        "send_message",
        "wait_for_mentions",
    ]
    tools = [tool for tool in tools if tool.name in coral_tool_names]
    tools += [get_all_github_files_tool, retrieve_github_file_content_tool]

    logger.info(f"Tools Description:\n{get_tools_description(tools)}")

    agent_executor = await create_doc_consistency_checker_agent(client, tools)

    while True:
        try:
            logger.info("Starting new agent invocation")
            await agent_executor.ainvoke({"agent_scratchpad": []})
            logger.info("Completed agent invocation, restarting loop")
            await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"Error in agent loop: {str(e)}")
            logger.error(traceback.format_exc())
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())


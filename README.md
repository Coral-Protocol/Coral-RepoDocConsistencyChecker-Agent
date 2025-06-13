## [Coral RepoDocConsistencyChecker Agent](https://github.com/Coral-Protocol/Coral-RepoDocConsistencyChecker-Agent)

The RepoDocConsistencyChecker Agent helps you evaluate whether the documentation in a specified GitHub repository and branch is up-to-date with respect to changes in a given list of files.

## Responsibility
The RepoDocConsistencyChecker Agent checks if documentation is consistent with recent code changes in a repository and branch, and recommends updates if needed.

## Details
- **Framework**: LangChain
- **Tools used**: PyGithub List File Tool, PyGithub Read File Tool, Coral Server Tools
- **AI model**: OpenAI GPT-4.1
- **Date added**: 02/05/25


## Use the Agent

### 1. Run Coral Server
<details>

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. In a new terminal, clone the repository:

```bash
# Clone the Coral Server repository
git clone https://github.com/Coral-Protocol/coral-server.git

# Navigate to the project directory
cd coral-server

# Run the server
./gradlew run
```
</details>

### 2. Run [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
<details>

The Interface Agent is required to interact with the RepoDocConsistencyChecker Agent. In a new terminal, clone the repository:

```bash
# Clone the Interface Agent repository
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git

# Navigate to the project directory
cd Coral-Interface-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync

# Run the agent using `uv`:
uv run python 0-langchain-interface.py
```
</details>

### 3. Run RepoDocConsistencyChecker Agent
<details>

In a new terminal, clone the repository:

```bash
# Clone the RepoDocConsistencyChecker Agent repository
git clone https://github.com/Coral-Protocol/Coral-RepoDocConsistencyChecker-Agent.git

# Navigate to the project directory
cd Coral-RepoDocConsistencyChecker-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```
This command will read the `pyproject.toml` file and install all specified dependencies in a virtual environment managed by `uv`.

Copy the client sse.py from utils to mcp package (Linux/Mac):
```bash
cp -r utils/sse.py .venv/lib/python3.10/site-packages/mcp/client/sse.py
```
OR for Windows:
```bash
cp -r utils\sse.py .venv\Lib\site-packages\mcp\client\sse.py
```
</details>

### 4. Configure Environment Variables
<details>

Get the API Keys:
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [GitHub Personal Access Token](https://github.com/settings/tokens)

Create a .env file in the project root:
```bash
cp -r .env.example .env
```

Add your API keys and any other required environment variables to the .env file.

Required environment variables:
- `OPENAI_API_KEY`
- `GITHUB_ACCESS_TOKEN`

</details>

### 5. Run Agent
<details>

Run the agent using `uv`:
```bash
uv run 6-langchain-RepoDocConsistencyCheckerAgent.py
```
</details>

### 6. Example
<details>

```bash
# Input:
Could you please help me check if the doc in the branch 'repo-understanding+unit-test-advice' of the repo 'renxinxing123/software-testing-agents-test' covered all changes from the updated file '4-langchain-RepoUnderstandingAgent.py' and '5-langchain-RepoUnitTestAdvisorAgent.py'.

# Output:
**Documentation Consistency Analysis for Updated Files:**

**Changed Files:**
- 4-langchain-RepoUnderstandingAgent.py
- 5-langchain-RepoUnitTestAdvisorAgent.py

**Relevant Documentation File Reviewed:**
- README.md

---

**Analysis:**

Both changed files implement new or updated agents for repository understanding and unit test advising. The README.md provides an overview of the agents, their responsibilities, and usage instructions for the system. It describes the roles of the "RepoUnderstandingAgent" and "RepoUnitTestAdvisorAgent" in the context of the multi-agent workflow, including their purpose and how they interact with the system.

**Findings:**
- The README.md does mention the existence and purpose of these agents, but it does not provide detailed usage instructions, configuration options, or specific workflow examples for these two agents.
- There is no section in the README.md that explains how to invoke these agents directly, what input parameters they require, or what output to expect.
- The agent scripts themselves contain detailed docstrings and workflow comments, but this information is not surfaced in the documentation.

**Recommendations:**
1. **Add Agent-Specific Sections:**
   - Add dedicated subsections in the README.md for "RepoUnderstandingAgent" and "RepoUnitTestAdvisorAgent".
   - Include a brief description, usage instructions (how to invoke, required arguments), and example input/output for each agent.
2. **Document Parameters and Workflow:**
   - Clearly document any environment variables, configuration, or prerequisites specific to these agents.
   - Provide a sample workflow showing how these agents fit into the overall system (e.g., how to trigger a repository analysis or test coverage evaluation).
3. **Update Usage Examples:**
   - If these agents can be invoked independently, add example commands or API calls.
   - If they are only used as part of the multi-agent workflow, clarify their role and how users interact with them.

**Summary:**
- The documentation is **partially up-to-date**: the agents are mentioned, but detailed usage and configuration instructions for the updated files are missing.
- Updating the README.md as recommended will improve clarity and help users leverage the new/updated agent functionalities.

Let me know if you need example documentation text or further breakdowns!
```
</details>

## Creator Details
- **Name**: Xinxing
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

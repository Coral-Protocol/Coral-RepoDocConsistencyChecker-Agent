## Responsibility

Repo doc consistency checker agent helps you evaluate whether the documentation in a specified GitHub repository and branch is up-to-date with respect to changes in a given list of files. Just provide the repository name, branch, and the list of changed files.

## Details

* Framework: LangChain
* Tools used: PyGithub List File Tool, PyGithub Read File Tool, Coral Server Tools
* AI model: OpenAI GPT-4.1
* Date added: 02/05/25
* Licence: MIT

## Use the Agent 
### 1. Clone & Install Dependencies

Run [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent)
<details>


If you are trying to run Open Deep Research agent and require an input, you can either create your agent which communicates on the coral server or run and register the Interface Agent on the Coral Server. In a new terminal clone the repository:


```bash
git clone https://github.com/Coral-Protocol/Coral-Interface-Agent.git
```
Navigate to the project directory:
```bash
cd Coral-Interface-Agent
```

Install `uv`:
```bash
pip install uv
```
Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

Configure API Key
```bash
export OPENAI_API_KEY=
```

Run the agent using `uv`:
```bash
uv run python 0-langchain-interface.py
```

</details>

Agent Installation

<details>

Clone the repository:
```bash
git clone https://github.com/Coral-Protocol/Coral-RepoDocConsistencyChecker-Agent.git
```

Navigate to the project directory:
```bash
cd Coral-RepoDocConsistencyChecker-Agent
```

Install `uv`:
```bash
pip install uv
```

Install dependencies from `pyproject.toml` using `uv`:
```bash
uv sync
```

This command will read the `pyproject.toml` file and install all specified dependencies in a virtual environment managed by `uv`.

Copy the client sse.py from utils to mcp package
```bash
cp -r utils/sse.py .venv/lib/python3.10/site-packages/mcp/client/sse.py
```

OR Copy this for windows
```bash
cp -r utils\sse.py .venv\Lib\site-packages\mcp\client\sse.py
```

</details>

### 2. Configure Environment Variables

<details>

Copy the example file and update it with your credentials:

```bash
cp .env.example .env
```

Required environment variables:

* `OPENAI_API_KEY`
* `GITHUB_ACCESS_TOKEN`

* **OPENAI_API_KEY:**
  Sign up at [platform.openai.com](https://platform.openai.com/), go to “API Keys” under your account, and click “Create new secret key.”

* **GITHUB_ACCESS_TOKEN:**
  Log in to [github.com](https://github.com/), go to **Settings → Developer settings → Personal access tokens**, then “Generate new token,” select the required scopes, and copy the generated token.

</details>
  
### 3. Run Agent
<details>

Run the agent using `uv`:
```bash
uv run 6-langchain-RepoDocConsistencyCheckerAgent.py
```

</details>

### 4. Example

<details>

Input:

Send the message to the interface agent:

```bash
Could you please help me check if the doc in the branch 'repo-understanding+unit-test-advice' of the repo 'renxinxing123/software-testing-agents-test' covered all changes from the updated file '4-langchain-RepoUnderstandingAgent.py' and '5-langchain-RepoUnitTestAdvisorAgent.py'.
```

Output:

```bash
**Documentation Consistency Analysis for Updated Files:**

**Changed Files:**
- 4-langchain-RepoUnderstandingAgent.py
- 5-langchain-RepoUnitTestAdvisorAgent.py

**Relevant Documentation File Reviewed:**
- README.md

---

**Analysis:**

Both changed files implement new or updated agents for repository understanding and unit test advising. The README.md provides an overview of the agents, their responsibilities, and usage instructions for the system. It describes the roles of the &quot;RepoUnderstandingAgent&quot; and &quot;RepoUnitTestAdvisorAgent&quot; in the context of the multi-agent workflow, including their purpose and how they interact with the system.

**Findings:**
- The README.md does mention the existence and purpose of these agents, but it does not provide detailed usage instructions, configuration options, or specific workflow examples for these two agents.
- There is no section in the README.md that explains how to invoke these agents directly, what input parameters they require, or what output to expect.
- The agent scripts themselves contain detailed docstrings and workflow comments, but this information is not surfaced in the documentation.

**Recommendations:**
1. **Add Agent-Specific Sections:**
   - Add dedicated subsections in the README.md for &quot;RepoUnderstandingAgent&quot; and &quot;RepoUnitTestAdvisorAgent&quot;.
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

## Creator details

* Name: Xinxing
* Affiliation: Coral Protocol
* Contact: [Discord](https://discord.com/invite/Xjm892dtt3)

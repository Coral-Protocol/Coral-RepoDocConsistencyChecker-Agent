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

### 3. Example

<details>

Repo doc consistency checker agent is supposed to take target changed file as input, sp please also run [Code diffs review agent](https://github.com/Coral-Protocol/Coral-CodeDiffReview-Agent) to get proper input.

Input:

```bash
#Send the message to the interface agent:
I created a new branch 'repo-understanding+unit-test-advice' in the repo 'renxinxing123/software-testing-agents-test' and opened a new PR (#2), could you please help me check if the relevant doc covered all the changes from the PR?
```

Output:

```bash
**Documentation Consistency Check for PR #2 (branch: 'repo-understanding+unit-test-advice')**

### Changed Files:
1. `4-langchain-RepoUnderstandingAgent.py` (new)
2. `5-langchain-RepoUnitTestAdvisorAgent.py` (new)

### Documentation Coverage:
- The main documentation file is `README.md`.
- The README describes the overall architecture, agent roles, and usage instructions for the system, including launching agents and running unit tests for PRs.
- However, the README **does not mention or document the two new agents**:
    - `RepoUnderstandingAgent` (4-langchain-RepoUnderstandingAgent.py)
    - `RepoUnitTestAdvisorAgent` (5-langchain-RepoUnitTestAdvisorAgent.py)
- There is no section describing their purpose, usage, workflow, or how to launch them.
- The agent roles listed in the README do not include these two new agents, nor are there updated instructions for launching or interacting with them.

### Recommendations:
1. **Update the README.md** to:
    - Add descriptions for `RepoUnderstandingAgent` and `RepoUnitTestAdvisorAgent`, including their responsibilities and how they fit into the system.
    - Update the &quot;Overview of Agents&quot; section to include these new agents.
    - Provide instructions for launching these agents, similar to the other agent scripts.
    - Optionally, add usage examples or scenarios where these agents are involved.

If you need suggested wording or a draft section for the README, let me know!

**Summary:**
The documentation is currently **outdated** with respect to the new agents added in this PR. Please update the README.md as described above.
```
</details>

## Creator details

* Name: Xinxing
* Affiliation: Coral Protocol
* Contact: [Discord](https://discord.com/invite/Xjm892dtt3)

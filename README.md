## [Coral RepoDocConsistencyChecker Agent](https://github.com/Coral-Protocol/Coral-RepoDocConsistencyChecker-Agent)
 
The RepoDocConsistencyChecker Agent helps you evaluate whether the documentation in a specified GitHub repository and branch is up-to-date with respect to changes in a given list of files

## Responsibility

The RepoDocConsistencyChecker Agent checks if documentation is consistent with recent code changes in a repository and branch, and recommends updates if needed.

## Details
- **Framework**: LangChain
- **Tools used**: PyGithub List File Tool, PyGithub Read File Tool, Coral Server Tools
- **AI model**: OpenAI GPT-4.1
- **Date added**: 02/05/25

## Setup the Agent

### 1. Clone & Install Dependencies

<details>  

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Coral-RepoDocConsistencyChecker-Agent.git

# Navigate to the project directory:
cd Coral-RepoDocConsistencyChecker-Agent

# Download and run the UV installer, setting the installation directory to the current one
curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=$(pwd) sh

# Create a virtual environment named `.venv` using UV
uv venv .venv

# Activate the virtual environment
source .venv/bin/activate

# install uv
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables

Get the API Keys:
- [OpenAI API Key](https://platform.openai.com/api-keys)
- [GitHub Personal Access Token](https://github.com/settings/tokens)

<details>

```bash
# Create .env file in project root
cp -r .env.example .env
```
</details>

## Run the Agent

You can run in either of the below modes to get your system running.  

- The Executable Model is part of the Coral Protocol Orchestrator which works with [Coral Studio UI](https://github.com/Coral-Protocol/coral-studio).  
- The Dev Mode allows the Coral Server and all agents to be seaprately running on each terminal without UI support.  

### 1. Executable Mode

Checkout: [How to Build a Multi-Agent System with Awesome Open Source Agents using Coral Protocol](https://github.com/Coral-Protocol/existing-agent-sessions-tutorial-private-temp) and update the file: `coral-server/src/main/resources/application.yaml` with the details below, then run the [Coral Server](https://github.com/Coral-Protocol/coral-server) and [Coral Studio UI](https://github.com/Coral-Protocol/coral-studio). You do not need to set up the `.env` in the project directory for running in this mode; it will be captured through the variables below.

<details>

For Linux or MAC:

```bash
# PROJECT_DIR="/PATH/TO/YOUR/PROJECT"

applications:
  - id: "app"
    name: "Default Application"
    description: "Default application for testing"
    privacyKeys:
      - "default-key"
      - "public"
      - "priv"

registry:
  repo_docconsistencychecker_agent:
    options:
      - name: "API_KEY"
        type: "string"
        description: "API key for the service"
      - name: "GITHUB_ACCESS_TOKEN"
        type: "string"
        description: "key for the github service"
    runtime:
      type: "executable"
      command: ["bash", "-c", "${PROJECT_DIR}/run_agent.sh main.py"]
      environment:
        - name: "API_KEY"
          from: "API_KEY"
        - name: "GITHUB_ACCESS_TOKEN"
          from: "GITHUB_ACCESS_TOKEN"
        - name: "MODEL_NAME"
          value: "gpt-4.1"
        - name: "MODEL_PROVIDER"
          value: "openai"
        - name: "MODEL_TOKEN"
          value: "16000"
        - name: "MODEL_TEMPERATURE"
          value: "0.3"

```

For Windows, create a powershell command (run_agent.ps1) and run:

```bash
command: ["powershell","-ExecutionPolicy", "Bypass", "-File", "${PROJECT_DIR}/run_agent.ps1","main.py"]
```

</details>

### 2. Dev Mode

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system and run below command in a separate terminal.

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

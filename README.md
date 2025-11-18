# Deep Agent Researcher (LangGraph via DeepAgents)

This project scaffolds a simple **Deep Agent** built with
LangChain DeepAgents and Tavily search. It uses a `.env` file to store API keys and
runs inside a Python virtual environment.

## 1. Create and activate a virtualenv

```bash
# From the project root
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Upgrade pip (optional, but recommended):

```bash
pip install --upgrade pip
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

This installs:

- `deepagents` (LangGraph-based deep agent harness)
- `tavily-python` (web search)
- `python-dotenv` (load `.env` file)

## 3. Set up your API keys with `.env`

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and set your real keys:
   ```env
   ANTHROPIC_API_KEY=sk-ant-...
   TAVILY_API_KEY=tvly-...
   ```

The file `src/config.py` uses `python-dotenv` to load this `.env` automatically and
validates that both variables are present. If anything is missing, it will raise a
clear error at startup.

## 4. Project structure

```text
deepagent_research/
├── .env.example          # Template for your environment variables
├── requirements.txt      # Python dependencies
└── src/
    ├── __init__.py
    ├── agent.py          # Creates the deep agent with `create_deep_agent`
    ├── config.py         # Loads/validates environment variables from .env
    ├── main.py           # Entry point: runs a sample query
    └── search_tools.py   # Tavily-backed `internet_search` tool
```

- **`search_tools.py`** defines the `internet_search` tool that calls Tavily.
- **`agent.py`** wires that tool into a Deep Agent using `create_deep_agent` and a
  research-oriented system prompt.
- **`main.py`** shows how to invoke the agent with a simple query.

## 5. Run the agent

From the project root (with the virtualenv activated and `.env` configured):

```bash
python -m src.main
```

You should see the agent's final answer printed to your terminal, based on the
query defined in `src/main.py`:

```python
query = "What is LangGraph?"
```

To change the question, edit `src/main.py` and modify `query` or wire the script
to read from `input()` or CLI arguments.

## 6. Next steps / extending the project

Some ideas for extending this scaffold:

- Add more tools (e.g., custom APIs, local file tools) and pass them in the
  `tools=[...]` list in `agent.py`.
- Customize the `research_instructions` system prompt to describe more complex
  workflows (planning, note-taking, critique loops, etc.).
- Expose the agent behind a FastAPI or Flask HTTP endpoint.
- Add subagents using DeepAgents' `subagents` parameter for specialized tasks.

This base project is intentionally minimal so you can grow it into your own
research or automation stack.

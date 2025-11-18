import os
from dotenv import load_dotenv

def _load_env() -> None:
    """Load environment variables from a .env file and validate required keys."""
    load_dotenv()

    required = ["ANTHROPIC_API_KEY", "TAVILY_API_KEY"]
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        missing_str = ", ".join(missing)
        raise RuntimeError(
            f"Missing required environment variable(s): {missing_str}.\n"
            "Create a .env file in the project root with these keys defined."
        )

# Load and validate on import so the rest of the app can assume keys are present.
_load_env()

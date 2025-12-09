import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    return {
        "openai_key": os.getenv("OPENAI_API_KEY"),
        "anthropic_key": os.getenv("ANTHROPIC_API_KEY")
    }

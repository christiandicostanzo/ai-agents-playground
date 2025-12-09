from strands import Agent, Task
from dotenv import load_dotenv
import os

load_dotenv()

def run_basic_agent():
    agent = Agent(
        role="Assistant",
        goal="Help users with their questions",
        backstory="You are a helpful AI assistant",
        llm_config={"model": "gpt-3.5-turbo", "api_key": os.getenv("OPENAI_API_KEY")}
    )
    
    task = Task(
        description="Answer: What is 2+2?",
        agent=agent
    )
    
    result = task.execute()
    print(result)
    
if __name__ == "__main__":
    run_basic_agent()

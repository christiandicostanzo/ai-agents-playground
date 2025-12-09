from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def run_basic_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "{input}"),
    ])
    
    # Add your agent logic here
    
if __name__ == "__main__":
    run_basic_agent()

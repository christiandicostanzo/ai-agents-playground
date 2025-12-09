import autogen
from dotenv import load_dotenv

load_dotenv()

def run_basic_agent():
    config_list = [{"model": "gpt-3.5-turbo", "api_key": "your_key"}]
    
    assistant = autogen.AssistantAgent(
        name="assistant",
        llm_config={"config_list": config_list}
    )
    
    user_proxy = autogen.UserProxyAgent(
        name="user_proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=1
    )
    
    # Add your agent logic here
    
if __name__ == "__main__":
    run_basic_agent()

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv; load_dotenv()
import os

os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

LLM = init_chat_model(
    model='mistral-small-latest'
)

my_agent = create_agent(
    model=LLM,
    system_prompt="You are my personal assistant"
)





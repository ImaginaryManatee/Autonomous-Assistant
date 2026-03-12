import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model = "claude-3-5-sonnet-20241022",
    temperature=0,
    max_tokens=1024
)

try:
    response = llm.invoke("Hello Calude, describe your role as my new AI agent.")
    print("Agnet Response:")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")
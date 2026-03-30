from google.adk.agents import Agent
from google.adk.models import Gemini

model = Gemini(model="gemini-pro")

def summarize_tool(text: str):
    prompt = f"Summarize this text in short:\n{text}"
    return prompt

agent = Agent(
    model=model,
    tools=[summarize_tool],
)
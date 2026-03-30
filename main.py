from fastapi import FastAPI
from agent import agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Agent is running 🚀"}

@app.get("/summarize")
def summarize(text: str):
    result = agent(text)
    return {"summary": result}
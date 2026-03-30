from fastapi import FastAPI, HTTPException
from agent import agent

app = FastAPI(title="AI Summarization Agent")

@app.get("/")
def home():
    return {"message": "AI Agent is running. Use POST /summarize"}

@app.post("/summarize")
async def summarize(data: dict):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    response = agent.run(text)
    return {"summary": response}
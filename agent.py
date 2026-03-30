import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def agent(text: str):
    prompt = f"Summarize this text in short:\n{text}"
    response = model.generate_content(prompt)
    return response.text
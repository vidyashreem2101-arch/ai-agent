import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def agent(text: str):
    try:
        prompt = f"Summarize this text in short:\n{text}"
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
        else:
            return "No response from AI"

    except Exception as e:
        return f"Error: {str(e)}"
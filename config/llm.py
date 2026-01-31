from google import genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini():
    return genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "temperature": 0.2,
            "max_output_tokens": 2048,
        }
    )

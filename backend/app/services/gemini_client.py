import google.generativeai as genai
from ..config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def analyze_text(text: str):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(text)
    return response.text

import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# listing available models
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

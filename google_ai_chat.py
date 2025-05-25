import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# listing available models
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

model = genai.GenerativeModel('gemini-2.0-flash')
prompt = 'Write an imaginary scientific paper that proposes a new theory of quantum mechanics.'
response = model.generate_content(prompt, stream=True)
for chunk in response:
    print(chunk.text, end='')

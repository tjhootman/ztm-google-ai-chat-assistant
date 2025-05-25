import os
import time
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
# from PIL import Image

# loading the API key and authenticating to Gemini
load_dotenv(find_dotenv(), override=True)
os.environ.get('GEMINI_API_KEY')

# Configuring the API key
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# listing available models
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

# text prompts
# model = genai.GenerativeModel('gemini-2.0-flash')
# prompt = 'Write an imaginary scientific paper that proposes a new theory of quantum mechanics.'
# response = model.generate_content(prompt, stream=True)
# for chunk in response:
#     print(chunk.text, end='')

# image prompts
# img = Image.open('salad.jpg')
# model = genai.GenerativeModel('gemini-2.0-flash')
# prompt = 'Summarize this image.'
# response = model.generate_content([prompt, img])
# print(response.text)

# chat conversation
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])
while True:
    prompt = input('User: ')
    if prompt.lower() not in ['exit', 'quit', 'bye']:
        response = chat.send_message(prompt)
        print(f'{chat.history[-1].role.capitalize()}: {chat.history[-1].parts[0].text}')
        print('\n' + '*' * 100 + '\n')
    else:
        print('Quitting...')
        time.sleep(2)
        print('Good-bye!')
        break

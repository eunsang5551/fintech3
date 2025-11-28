import os
import google.generativeai as genai

os.environ["GEMINI_API_KEY"] = "AIzaSyDjL5XQcCkAqlX9Rmp0n2DQpbekgyTbBhk"
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

client = genai.Client(api_key=GEMINI_API_KEY)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="테스트!"
)
print(response.text)

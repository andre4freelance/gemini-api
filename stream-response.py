from google import genai
from dotenv import load_dotenv

# Inisialisasi client
load_dotenv()
client = genai.Client()

response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents=["Explain how AI works"]
)
for chunk in response:
    print(chunk.text, end="")
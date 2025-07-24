from google import genai
from dotenv import load_dotenv

# Inisialisasi client
load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Tell me about bitcoin"
)
print(response.text)
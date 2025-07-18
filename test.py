from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="API KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Sapa aku jika ini sudah berhasil"
)
print(response.text)
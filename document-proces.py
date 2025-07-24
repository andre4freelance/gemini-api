from google import genai
from google.genai import types
import pathlib
from dotenv import load_dotenv


# Initialize client
load_dotenv()
client = genai.Client()

# Retrieve and encode the PDF byte
filepath = pathlib.Path('Gre-tunnel.pdf')

# Input prompt
prompt = input("Describe what you want Gemini do from this document: ")

prompt = prompt,
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=filepath.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)
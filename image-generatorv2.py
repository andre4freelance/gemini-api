from google import genai
from googAle.genai import types
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv

# Inisialisasi client
load_dotenv()
client = genai.Client()

# Ambil input dari pengguna setelah program dijalankan
contents = input("Describe the image you want Gemini to generate: ")

# Kirim permintaan ke model
response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=contents,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

# Tampilkan hasil
for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save('gemini-native-image.png')
        image.show()
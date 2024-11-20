# Galih Hermawan - https://galih.eu

import google.generativeai as genai  
import PIL.Image

# Token API ditulis langsung di sini untuk kemudahan (tidak disarankan untuk produksi)  
API_KEY = "API_KEY_ANDA"  

# Konfigurasikan API Key Anda
genai.configure(api_key=API_KEY)

# Inisialisasi model
model = genai.GenerativeModel('gemini-1.5-flash')

# Tentukan alamat dan nama fail gambar (Perhatikan penulisan alamat relatif atau absolut).
# Fungsi PIL di sini digunakan untuk membuka gambar dari file.
#gambar = PIL.Image.open("d:/PythonKu/[_share_]/Proyek_Gemini_Api/kode_asli/gambar/kabah.jpg")
gambar = PIL.Image.open("./gambar/kabah.jpg")

# Fungsi ini digunakan untuk menghasilkan konten berdasarkan input yang diberikan.
response = model.generate_content(["Buatlah deskripsi mengenai gambar ini!", gambar])

print(response.text)
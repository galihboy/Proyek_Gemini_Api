# Galih Hermawan - https://galih.eu

import google.generativeai as genai  

# Token API ditulis langsung di sini untuk kemudahan (tidak disarankan untuk produksi)  
API_KEY = "API_KEY_ANDA"  

# Konfigurasikan API Key Anda
genai.configure(api_key=API_KEY)

# Inisialisasi model
model = genai.GenerativeModel('gemini-1.5-flash')

# Pertanyaan atau instruksi
prompt = "Jelaskan tentang kecerdasan buatan secara singkat!"

# Mendapatkan respons
respons = model.generate_content(prompt)

# Menampilkan hasilnya
print("Prompt:", prompt)
print("\nJawaban:", respons.text)
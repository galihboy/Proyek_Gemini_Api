# Galih Hermawan - https://galih.eu
 
import google.generativeai as genai

# Token API ditulis langsung di sini untuk kemudahan (tidak disarankan untuk produksi)  
API_KEY = "AIzaSyBomyKrBlHUaRkzLf7Iu4aJEcibhxgneM4"  

# Konfigurasikan API Key Anda
API_KEY = "API_KEY_ANDA"  

# Inisialisasi model
model = genai.GenerativeModel('gemini-1.5-pro')

# Memulai chat dengan history kosong
chat = model.start_chat(history=[])

def lakukan_dialog():
    print("Mulai dialog dengan Gemini AI (ketik 'keluar' untuk mengakhiri)")
    
    while True:
        # Input pengguna
        pertanyaan = input("\nAnda: ")
        
        # Cek apakah ingin keluar
        if pertanyaan.lower() == 'keluar':
            print("Dialog berakhir.")
            break
        
        # Kirim pertanyaan dan dapatkan respons
        respons = chat.send_message(pertanyaan)
        
        # Tampilkan respons
        print("\nGemini:", respons.text)

# Jalankan dialog
if __name__ == "__main__":
    lakukan_dialog()
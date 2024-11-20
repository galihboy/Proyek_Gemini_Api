# Galih Hermawan - https://galih.eu
 
import google.generativeai as genai

# Token API ditulis langsung di sini untuk kemudahan (tidak disarankan untuk produksi)  
API_KEY = "API_KEY_ANDA"  

# Konfigurasikan API Key Anda
API_KEY = "API_KEY_ANDA"  

# Fungsi untuk menampilkan model yang tersedia
def tampilkan_model():
    # Dapatkan daftar model
    for model in genai.list_models():
        # Filter hanya model yang dapat di-generate
        if 'generateContent' in model.supported_generation_methods:
            print(f"Model Name: {model.name}")
            print(f"Description: {model.description}")
            print(f"Input Token Limit: {model.input_token_limit}")
            print(f"Output Token Limit: {model.output_token_limit}")
            print("-" * 50)

# Jalankan fungsi
if __name__ == "__main__":
    tampilkan_model()
import requests
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Umico API bilgileri
API_KEY = os.getenv("API_KEY", "932c5778-16aa-4174-a35b-811f19e328dc")
API_URL = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection"

def update_prices(product_offers):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=product_offers)
        response.raise_for_status()  # Hataları yakala
        print("✅ Prices updated successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ An error occurred:", e)

def main():
    # Ürün teklifleri (örnek veri)
    product_offers = {
        "product_offers": {
            "payload": [
                {
                    "gtin": "56498423156",  # Ürün barkodu (zorunlu)
                    "old_price": 120,       # Eski fiyat (opsiyonel)
                    "retail_price": 100,    # Yeni fiyat (zorunlu değil ama tavsiye edilir)
                    "qty": 1,               # Stok miktarı (zorunlu değil ama gerekli)
                    "installment_enabled": True,  # Taksit var mı (boolean olmalı)
                    "max_installment": 18,        # Maksimum taksit sayısı
                    "discount_effective_start_date": "2024-12-12 00:00:00",  # İndirim başlangıç
                    "discount_effective_end_date": "2024-12-12 23:59:59"      # İndirim bitiş
                }
            ]
        }
    }

    update_prices(product_offers)

if __name__ == "__main__":
    main()
import requests
import os
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Umico API bilgileri
API_KEY = os.getenv("UMICO_API_KEY", "932c5778-16aa-4174-a35b-811f19e328dc")
API_URL = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection"

def update_prices(product_offers):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=product_offers)
        response.raise_for_status()  # Hataları yakala
        print("✅ Prices updated successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ An error occurred:", e)

def main():
    # Ürün teklifleri (örnek veri)
    product_offers = {
        "product_offers": {
            "payload": [
                {
                    "gtin": "56498423156",  # Ürün barkodu (zorunlu)
                    "old_price": 120,       # Eski fiyat (opsiyonel)
                    "retail_price": 100,    # Yeni fiyat (zorunlu değil ama tavsiye edilir)
                    "qty": 1,               # Stok miktarı (zorunlu değil ama gerekli)
                    "installment_enabled": True,  # Taksit var mı (boolean olmalı)
                    "max_installment": 18,        # Maksimum taksit sayısı
                    "discount_effective_start_date": "2024-12-12 00:00:00",  # İndirim başlangıç
                    "discount_effective_end_date": "2024-12-12 23:59:59"      # İndirim bitiş
                }
            ]
        }
    }

    update_prices(product_offers)

if __name__ == "__main__":
    main()

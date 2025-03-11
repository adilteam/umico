import requests
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем API-ключ
API_KEY = os.getenv("932c5778-16aa-4174-a35b-811f19e328dc")
if not API_KEY:
    raise ValueError("❌ UMICO_API_KEY не найден в .env")

API_URL = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection"

def update_prices(product_offers):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=product_offers)
        response.raise_for_status()  
        print("✅ Prices updated successfully:", response.json())
    except requests.exceptions.RequestException as e:
        print("❌ An error occurred:", e)

def main():
    product_offers = {
        "payload": [  # Убрал лишнюю обертку "product_offers"
            {
                "gtin": "56498423156",
                "old_price": 120,
                "retail_price": 100,
                "qty": 1,
                "installment_enabled": True,
                "max_installment": 18,
                "discount_effective_start_date": "2024-12-12 00:00:00",
                "discount_effective_end_date": "2024-12-12 23:59:59"
            }
        ]
    }

    update_prices(product_offers)

if __name__ == "__main__":
    main()

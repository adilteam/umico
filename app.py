import requests
import os
from dotenv import load_dotenv
import json

# Загружаем переменные окружения
load_dotenv()

# Получаем API-ключ по имени переменной
API_KEY = os.getenv("API_KEY")  # Должно быть имя переменной, а не сам ключ

# Проверка, загружен ли API_KEY
if not API_KEY:
    raise ValueError("❌ API_KEY не найден в .env")

API_URL = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection"

def update_prices(product_offers_data):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        # Отправляем POST-запрос
        print(f"Отправка данных: {json.dumps(product_offers_data, indent=2)}")
        response = requests.post(API_URL, headers=headers, json=product_offers_data)
        
        # Вывод информации о ответе
        print("Response Status Code:", response.status_code)
        print("Response Headers:", dict(response.headers))
        print("Response Text:", response.text)
        
        # Проверка на ошибку
        response.raise_for_status()

        # Если запрос успешен, печатаем JSON-ответ
        print("✅ Prices updated successfully:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error details: {e.response.text}")
        return None

def main():
    # Структура данных согласно документации
    product_offers_data = {
        "product_offers": {
            "payload": [
                {
                    "gtin": "56498423156",
                    "retail_price": 100.0,
                    "old_price": 120.0,
                    "qty": 1,
                    "installment_enabled": "true",  # Как строка, согласно документации
                    "max_installment_months": 18,  # Правильное название поля из документации
                    "discount_effective_start_date": "12.12.2024 0:00:00",  # Формат даты из документации
                    "discount_effective_end_date": "12.12.2024 23:59:59"  # Формат даты из документации
                }
            ]
        }
    }

    update_prices(product_offers_data)

if __name__ == "__main__":
    main()

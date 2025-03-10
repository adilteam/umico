import requests

# API açarının təyini
api_key = 'bc7cc0c7-d17c-420d-b838-ce63daaa6b7f'
url = 'https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection'

def update_prices(product_offers):
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }
    response = requests.post(url, headers=headers, json=product_offers)

    if response.status_code == 200:
        print("Prices updated successfully")
        print(response.json())
    elif response.status_code == 403:
        print(f"Failed to update prices: {response.status_code}")
        print(response.json())
        print("Check if your IP address is allowed and your API key is correct.")
    else:
        print(f"Failed to update prices: {response.status_code}")
        try:
            print(response.json())
        except requests.exceptions.JSONDecodeError:
            print("No JSON response received")

def main():
    product_offers = {
        "product_offers": [
            {
                "payload": [
                    {
                        "retail_price": 1854,
                        "old_price": 2846,
                        "quantity": 1,
                        "maximum_installment_month": 18,
                        "installment_enabled": True,
                        "gtin": "56498423156",
                        "discount_effective_start_date": "12.12.2024 0:00:00",
                        "discount_effective_end_date": "12.12.2024 23:59:59"
                    }
                ]
            }
        ]
    }
    update_prices(product_offers)

if __name__ == "__main__":
    main()

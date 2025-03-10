mport requests

# Düzgün dəyişən adı ilə API açarının təyini
api_key = '932c5778-16aa-4174-a35b-811f19e328dc'
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
                        "gtin": "194850877209",
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

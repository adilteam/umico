
import requests

def update_prices(product_offers):
    url = "https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collectio"
    headers = {
        "x-api-key": "bc7cc0c7-d17c-420d-b838-ce63daaa6b7f",  # Ensure this is a single string
    }
    response = requests.post(url, headers=headers, json=product_offers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()

def main():
    product_offers = {
        # Your product offers data here
    }
    try:
        result = update_prices(product_offers)
        print("Prices updated successfully:", result)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

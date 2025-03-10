import requests

# Umico API endpoint and API key
X-api_endpoint = 'https://catalog-admin-web-stage.umico.az/api/v1/product_offers/upsert_collection'
X-api_key = '932c5778-16aa-4174-a35b-811f19e328dc'

# Function to get competitor prices (dummy function, replace with actual logic)
def get_competitor_price(gtin):
    # Use the actual logic to get competitor prices
    # This is a dummy implementation
    competitor_prices = {
        "56498423156": 99
    }
    return competitor_prices.get(gtin, 0)

# Function to update product prices
def update_prices(product_offers):
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json'
    }
    
    for offer in product_offers:
        gtin = offer['gtin']
        old_price = offer['old_price']
        retail_price = offer['retail_price']
        
        # Get competitor price
        competitor_price = get_competitor_price(gtin)
        
        if competitor_price > 0:
            # Set new price 1 qəpik lower than competitor price
            new_price = competitor_price - 0.01
            offer['retail_price'] = new_price

    payload = {
        "product_offers": {
            "payload": product_offers
        }
    }
    
    response = requests.post(api_endpoint, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Prices updated successfully")
    else:
        print(f"Failed to update prices: {response.status_code}")
        print(response.json())

# Example product offers
product_offers = [
    {
        "gtin": "56498423156",
        "old_price": 120,
        "retail_price": 100,
        "qty": 1
    }
]

# Update prices
update_prices(product_offers)

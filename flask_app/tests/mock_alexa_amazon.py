import requests
import json

# Base URL of the Flask application
base_url = 'http://localhost:3838'

# Mock payload for adding a product to Amazon list
add_product_payload = {
    "product_name": "Example Product"
}

# Send the mock request to the Flask application
response = requests.post(f'{base_url}/amazon/add_product', json=add_product_payload)

print("Status Code:", response.status_code)
print("Response:", response.json())

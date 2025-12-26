
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <amount>")
        sys.exit(1)

    try:
        # FIX 1: Access the specific argument at index 1
        amount = float(sys.argv[1])
        get_price(amount)
    except ValueError:
        print('Command-line argument is not a number')
        sys.exit(1)

def get_price(amount):
    url = 'https://rest.coincap.io/v3/assets?search=bitcoin'
    api_key = 'a802726096abc81195f81f310df291ff8ecd9036637f9d149fa351c72ae71f6d'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            price_usd = float(data['data'][0]['priceUsd'])
            total_value = amount * price_usd
            # Format to two decimal places, with commas, no trailing zeros after decimal
            formatted = f"${total_value:,.2f}"
            print(formatted)
        else:
            print("Could not retrieve Bitcoin price.")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

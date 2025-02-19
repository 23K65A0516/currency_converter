import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and to_currency in data["rates"]:
        return data["rates"][to_currency]
    else:
        print("Error: Unable to get exchange rate.")
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# Example usage
from_currency = "USD"
to_currency = "EUR"
amount = 100

converted_amount = convert_currency(amount, from_currency, to_currency)
if converted_amount:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")

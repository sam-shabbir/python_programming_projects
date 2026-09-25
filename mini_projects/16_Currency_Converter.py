# 16 - Currency Converter
#
# REWRITE: the original used free.currconv.com, which has shut down and needed an API key.
# This version uses Frankfurter (https://frankfurter.dev) - free, no API key, no sign-up.
# Its rates come from the European Central Bank and update once per working day.

from requests import get # pip install requests - get() sends a GET request to a URL and returns the response

BASE_URL = "https://api.frankfurter.dev/v1/" # every endpoint below is added onto the end of this


def get_currencies(): # returns a sorted list of (code, name) pairs, e.g. ("GBP", "British Pound")
    url = BASE_URL + "currencies"
    data = get(url, timeout=10).json() # .json() turns the text reply into a Python dictionary: {"GBP": "British Pound", ...}

    data = list(data.items()) # .items() gives (key, value) pairs; list() lets us sort them
    data.sort() # tuples sort by their first item, so this sorts alphabetically by currency code

    return data


def print_currencies(currencies):
    for code, name in currencies: # each item is a (code, name) tuple, so we "unpack" it into two variables
        print(f"{code} - {name}")


def exchange_rate(currency1, currency2): # how much 1 unit of currency1 is worth in currency2
    if currency1 == currency2: # the API refuses same-currency pairs, but the answer is obviously 1
        print(f"{currency1} -> {currency2} = 1")
        return 1.0

    # `params` builds the "?from=USD&to=GBP" part of the URL for us
    response = get(BASE_URL + "latest", params={"from": currency1, "to": currency2}, timeout=10)

    # .ok is True for successful replies (status codes 200-399).
    # An unknown code like "XYZ" makes the API reply 404 "not found" instead.
    if not response.ok:
        print("Invalid currencies.")
        return None # None means "no answer" - convert() checks for this

    data = response.json() # e.g. {"amount": 1.0, "base": "USD", "date": "2026-09-24", "rates": {"GBP": 0.75645}}
    rate = data["rates"][currency2] # dig into the nested dictionary to get the number
    print(f"{currency1} -> {currency2} = {rate}  (as of {data['date']})")

    return rate


def convert(currency1, currency2, amount):
    # Convert the amount FIRST, so a typo doesn't waste an API call
    try:
        amount = float(amount) # float, not int, because money has decimals (e.g. 12.50)
    except ValueError: # float("abc") raises ValueError - we catch it instead of crashing
        print("Invalid amount.")
        return None

    rate = exchange_rate(currency1, currency2)
    if rate is None: # exchange_rate() already printed why it failed
        return None

    converted_amount = rate * amount
    print(f"{amount:.2f} {currency1} is equal to {converted_amount:.2f} {currency2}") # :.2f shows 2 decimal places, like real money
    return converted_amount


def main():
    currencies = get_currencies() # download the list once at the start, rather than every time "list" is typed

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper() # .upper() because the API expects codes like "GBP"
            amount = input(f"Enter an amount in {currency1}: ") # input() always returns a string - convert() turns it into a number
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__": # only run main() when this file is run directly, not when it's imported
    main()

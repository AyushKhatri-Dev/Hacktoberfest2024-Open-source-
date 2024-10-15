from forex_python.converter import CurrencyRates, CurrencyCodes

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    try:
        c = CurrencyRates()
        converted_amount = c.convert(from_currency.upper(), to_currency.upper(), amount)

        # Display the converted amount
        code = CurrencyCodes()
        symbol = code.get_symbol(to_currency.upper())
        print(f"{amount} {from_currency.upper()} is equal to {symbol}{converted_amount:.2f} {to_currency.upper()}")
    except Exception as e:
        print(f"Error: {e}")

# Main function to take user input
def main():
    print("Welcome to the Currency Converter!")
    
    try:
        # Get user inputs
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency you have (e.g., USD, INR, EUR): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., USD, INR, EUR): ").upper()

        # Convert the currency
        convert_currency(amount, from_currency, to_currency)
    
    except ValueError:
        print("Please enter a valid number for the amount.")

if __name__ == "__main__":
    main()

import requests
import json


#Dictonary of available currency code and names
available_currency = {"AUD":"Australian Dollar","BGN":"Bulgarian Lev","BRL":"Brazilian Real",
                      "CAD":"Canadian Dollar","CHF":"Swiss Franc","CNY":"Chinese Renminbi Yuan",
                      "CZK":"Czech Koruna","DKK":"Danish Krone","EUR":"Euro","GBP":"British Pound",
                      "HKD":"Hong Kong Dollar","HUF":"Hungarian Forint","IDR":"Indonesian Rupiah",
                      "ILS":"Israeli New Sheqel","INR":"Indian Rupee","ISK":"Icelandic Króna",
                      "JPY":"Japanese Yen","KRW":"South Korean Won","MXN":"Mexican Peso","MYR":
                      "Malaysian Ringgit","NOK":"Norwegian Krone","NZD":"New Zealand Dollar",
                      "PHP":"Philippine Peso","PLN":"Polish Złoty","RON":"Romanian Leu","SEK":
                      "Swedish Krona","SGD":"Singapore Dollar","THB":"Thai Baht","TRY":"Turkish Lira",
                      "USD":"United States Dollar","ZAR":"South African Rand"}

#To handle, validate user_ input
def user_input():
    print("Welcome! \nThis code is to convert a currency's value to another currency's. Please follow the instructions. Note: You can either type in currency name or code.")
    while True:
        currency_from = input("Currency you want to convert from: ").lower().strip()
        currency_code = None
        #If the user put in names
        if currency_from.upper() in available_currency:
            currency_code = currency_from.upper()
        else:
            #Check against currency names
            for code, name in available_currency.items():
                if currency_from == name.lower():
                    currency_code = code
                    break
        if not currency_code:
            print("Please input available currency.") 
        else:
            break
    while True:
        currency_to = input("Currency you want to convert to: ")
        currency_to_code = None
        #if the user put in names
        if currency_to.upper() in available_currency:
            currency_to_code = currency_to.upper()
        else:
            #Check against currency names
            for code, name in available_currency.items():
                if currency_to == name.lower(): #Checking if the user's input (converte to lowercase) matches the lowercase version of the name
                    currency_to_code = code #Once find the matching name, we grab the corresponding code 
                    break
        if not currency_to_code:
            print("Please input available currency.")
        else:
            break
    while True:
        try:
            amount = float(input(f"Amount of {currency_code} that you want to convert: "))
            if amount <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except (ValueError, TypeError):
            print('Please type in a valid number.')
    
    return currency_code, currency_to_code, amount
         
#To get conversion rates
#Be able to change the base(currency_from)
def rate_convert(currency_code, currency_to_code, amount):
     try:
         x = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={currency_code}&to={currency_to_code}")
         data = x.json()
         amount_to = data['rates'][currency_to_code]
         return amount_to
     except requests.RequestException:
          print('Request Exception')


#To perform conversion
def conversion():
     ...

#To print output
currency_from, currency_to, amount = user_input()
amount_to = rate_convert(currency_from, currency_to, amount)
print(f"{amount} {currency_from} = {amount_to} {currency_to}")
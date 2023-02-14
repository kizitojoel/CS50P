# Api for the exchange rate gmail is jobethkizito@gmail.com
# Password for the API key is: Exg.J5XWyF#x#!f
# API_KEY = 0916f2916f348a6de277d120

import requests
import os
import json
import csv
from datetime import datetime
# Function for the main program loop
def main():
    pass

# Should enable a user to begin with specific transactions
def default_settings():
    with open("transactions.csv", "a") as file1:
        fieldnames = ["date", "currency", "quantity", "rate",  "cost", "balance"]
        writer = csv.DictWriter(file1, fieldnames=fieldnames)
        writer.writerow(
            {
                "date": datetime.now().strftime("%H:%M--%d-%m-%Y"),
                "currency": example_quote["base_code"],
                "quantity":10000,
                "rate": "-",
                "cost": "-",
                "balance": 10000
            }
        )

def get_balance():
    sum = 0
    with open("transactions.csv", "r") as f:
        fieldnames = ["date", "currency", "quantity", "rate",  "cost", "balance"]
        reader = csv.DictReader(f, fieldnames=fieldnames)
        print(reader)
        for row in reader:
            try:
                cost = float(row["cost"])
                sum += cost
            except ValueError:
                continue
    return sum


def buy(currency, amount:int) -> None:
    # The variables this function will need, are the type and amount of currency the user is buying.

    # The user makes a transaction, and we get the quote from the quote() function

    # The script opens the file and records the details of the transaction
    balance = get_balance()
    with open("transactions.csv", "a") as file1:
        fieldnames = ["date", "currency", "quantity", "rate",  "cost", "balance"]
        writer = csv.DictWriter(file1, fieldnames=fieldnames)


        #Get the current date as a string
        current_date = datetime.now()
        date_string = current_date.strftime("%H:%M--%d-%m-%Y")
        rate = convert(currency)
        # I want the rate to show the amount I am dividing by, as that is more intuitive

        #Call the convert function
        writer.writerow(
            {
                "date": date_string,
                "currency": currency,
                "quantity":amount,
                "rate": rate,
                "cost": round(-abs(amount / rate), 2),
                "balance": round(balance - abs(amount / rate), 2) 
            }
        )
        

"""
Function for selling currency
It is intuitively just 
"""
def sell():
    pass

def quote(base_currency):
    r = requests.get(f"https://v6.exchangerate-api.com/v6/{os.environ.get('API_KEY')}/latest/{base_currency}")
    data = r.json()
    return data


def record():
    pass



example_quote = {'result': 'success', 
'documentation': 'https://www.exchangerate-api.com/docs', 'terms_of_use': 'https://www.exchangerate-api.com/terms', 
'time_last_update_unix': 1676332802, 'time_last_update_utc': 'Tue, 14 Feb 2023 00:00:02 +0000', 'time_next_update_unix': 1676419202, 
'time_next_update_utc': 'Wed, 15 Feb 2023 00:00:02 +0000', 'base_code': 'KES', 'conversion_rates': {'KES': 1, 'AED': 0.02933, 
'AFN': 0.7173, 'ALL': 0.8671, 'AMD': 3.1595, 'ANG': 0.01429, 'AOA': 4.0471, 'ARS': 1.5211, 'AUD': 0.01152, 'AWG': 0.01429, 
'AZN': 0.01363, 'BAM': 0.01462, 'BBD': 0.01597, 'BDT': 0.8493, 'BGN': 0.01462, 'BHD': 0.003002, 'BIF': 16.5482, 'BMD': 0.007985, 
'BND': 0.01063, 'BOB': 0.05525, 'BRL': 0.04114, 'BSD': 0.007985, 'BTN': 0.6601, 'BWP': 0.1039, 'BYN': 0.02032, 'BZD': 0.01597, 
'CAD': 0.01067, 'CDF': 16.6159, 'CHF': 0.007376, 'CLP': 6.3791, 'CNY': 0.05449, 'COP': 38.2528, 'CRC': 4.6139, 'CUP': 0.1916, 
'CVE': 0.8245, 'CZK': 0.1757, 'DJF': 1.4192, 'DKK': 0.05578, 'DOP': 0.4495, 'DZD': 1.0917, 'EGP': 0.2437, 'ERN': 0.1198, 'ETB': 0.429, 
'EUR': 0.007477, 'FJD': 0.01746, 'FKP': 0.00661, 'FOK': 0.05578, 'GBP': 0.00661, 'GEL': 0.02116, 'GGP': 0.00661, 'GHS': 0.09819, 
'GIP': 0.00661, 'GMD': 0.4993, 'GNF': 67.9647, 'GTQ': 0.06262, 'GYD': 1.6864, 'HKD': 0.06269, 'HNL': 0.1967, 'HRK': 0.05634, 
'HTG': 1.2071, 'HUF': 2.8559, 'IDR': 121.9194, 'ILS': 0.02781, 'IMP': 0.00661, 'INR': 0.6601, 'IQD': 11.645, 'IRR': 348.6691, 
'ISK': 1.1409, 'JEP': 0.00661, 'JMD': 1.2325, 'JOD': 0.005662, 'JPY': 1.0536, 'KGS': 0.6935, 'KHR': 32.6096, 'KID': 0.01152, 
'KMF': 3.6786, 'KRW': 10.187, 'KWD': 0.002444, 'KYD': 0.006654, 'KZT': 3.6079, 'LAK': 135.368, 'LBP': 12.0379, 'LKR': 2.8981, 
'LRD': 1.2553, 'LSL': 0.1431, 'LYD': 0.03827, 'MAD': 0.08214, 'MDL': 0.1501, 'MGA': 34.4382, 'MKD': 0.4589, 'MMK': 16.7632, 
'MNT': 28.1024, 'MOP': 0.06457, 'MRU': 0.2903, 'MUR': 0.3625, 'MVR': 0.1231, 'MWK': 8.1222, 'MXN': 0.1475, 'MYR': 0.03484, 
'MZN': 0.5113, 'NAD': 0.1431, 'NGN': 3.6745, 'NIO': 0.2925, 'NOK': 0.08106, 'NPR': 1.0562, 'NZD': 0.01248, 'OMR': 0.00307, 
'PAB': 0.007985, 'PEN': 0.03064, 'PGK': 0.02812, 'PHP': 0.4378, 'PKR': 2.1454, 'PLN': 0.03577, 'PYG': 58.1915, 'QAR': 0.02907, 
'RON': 0.03627, 'RSD': 0.8769, 'RUB': 0.5812, 'RWF': 8.6682, 'SAR': 0.02994, 'SBD': 0.06655, 'SCR': 0.1096, 'SDG': 4.1941, 
'SEK': 0.08344, 'SGD': 0.01063, 'SHP': 0.00661, 'SLE': 0.1584, 'SLL': 158.3535, 'SOS': 4.5449, 'SRD': 0.2601, 'SSP': 5.8741, 
'STN': 0.1832, 'SYP': 20.032, 'SZL': 0.1431, 'THB': 0.2675, 'TJS': 0.08262, 'TMT': 0.02796, 'TND': 0.02492, 'TOP': 0.01866, 
'TRY': 0.1488, 'TTD': 0.05425, 'TVD': 0.01152, 'TWD': 0.2415, 'TZS': 18.6726, 'UAH': 0.2934, 'UGX': 29.4012, 'USD': 0.007985, 
'UYU': 0.3128, 'UZS': 90.5751, 'VES': 0.1937, 'VND': 188.139, 'VUV': 0.937, 'WST': 0.02144, 'XAF': 4.9048, 'XCD': 0.02156, 
'XDR': 0.005964, 'XOF': 4.9048, 'XPF': 0.8923, 'YER': 1.9983, 'ZAR': 0.1431, 'ZMW': 0.1522, 'ZWL': 6.6598}}


def convert(output, inverse=False): # The inverse optional parameter
    # if example_quote['result'] == "success":
    #     try:
            
    #         else:
    #             print(f"1 {source} is equal to {example_quote['conversion_rates'][output]} {output}")
    #             return example_quote['conversion_rates'][output]
    #     except KeyError:
    #         print("Key not found")
            
    # else:
    #     print("Error: Unsuccessful request")

    if inverse:
        print(f"1 {output} is equal to {round((1 / example_quote['conversion_rates'][output]), 4)} {example_quote['base_code']}")
        return round((1 / example_quote['conversion_rates'][output]), 4)
    else:
        print(f"1 {example_quote['base_code']} is equal to {example_quote['conversion_rates'][output]} {output}")
        return example_quote["conversion_rates"][output]

print(convert("KES", inverse=True))
buy("USD", 10)











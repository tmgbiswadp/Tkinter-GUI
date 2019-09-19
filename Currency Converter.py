# Python program to get the real-time
# currency exchange rate
import requests

# Function to get real time currency exchange
def convert(from_currency, to_currency, api_key):
    # importing required libraries

    # base_url variable store base url
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # main_url variable store complete url
    main_url = url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    # get method of requests module

    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(" Result before parsing the json data :\n", result)

    print("\n After parsing : \n Realtime Currency Exchange Rate for",
          result["Realtime Currency Exchange Rate"]
          ["2. From_Currency Name"], "TO",
          result["Realtime Currency Exchange Rate"]
          ["4. To_Currency Name"], "is",
          result["Realtime Currency Exchange Rate"]
          ['5. Exchange Rate'], to_currency)


# Driver code
if __name__ == "__main__":
    # currency code
    from_currency = "USD"
    to_currency = "INR"

    # enter your api key here
    api_key = "4C78DI2ZL0EW5CVB"

    # function calling
    convert(from_currency, to_currency, api_key)

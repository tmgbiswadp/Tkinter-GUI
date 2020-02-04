# Python program to get the real-time
# currency exchange rate and convert the currency
import requests
import tkinter as tk
from tkinter import Tk

class Currency_converter:
    to_currency='nice'
    currencytobeconverted=1

    def __init__(self,root):
        self.root=root
        root.title("***Currency Converter***")
        root.geometry("300x140")
        root.resizable(0,0)
 
        tk.Label(root, text="Currency from").grid(row=0, column=1)
        tk.Label(root, text="Currency to").grid(row=1, column=1)

        self.currencyfromentry = tk.Entry(root)
        self.currencyfromentry.grid(row=0, column=2)
        currencyfrom = tk.Entry(root)

        currencyto = tk.Entry(root)
        self.currencytoentry = tk.Entry(root)
        self.currencytoentry.grid(row=1, column=2)

        currencyfromvariable = tk.StringVar(root)
        currencyfromvariable.set("NPR")

        currencytovariable = tk.StringVar(root)
        currencytovariable.set("INR")

        currencyfrom = tk.OptionMenu(root, currencyfromvariable, "NPR", "INR", "USD")
        currencyfrom.grid(row=0, column=3)

        currencyto = tk.OptionMenu(root, currencytovariable, "NPR", "INR", "USD")
        currencyto.grid(row=1, column=3)

        convertbtn = tk.Button(root, text="Convert", bg="orange", command = lambda:self.getvaluesfromdropdown(currencyfromvariable.get(), currencytovariable.get()))
        convertbtn.grid(row=2, column=1)

        clearbtn = tk.Button(root, text="Clear", bg="orange", command=self.clear)
        clearbtn.grid(row=2, column=2)

    def getvaluesfromdropdown(self, one, two):
        file_object = open("api.txt","r")
        api_value = file_object.readline()
        self.convert(one,two, api_value)

        # Function to get real time currency exchange
    def convert(self, from_currency, to_currency, api_key):
        # importing required libraries

        # base_url variable store base url
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

        # main_url variable store complete url
        main_url = url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

        # get method of requests module

        # return response object
        req_ob = requests.get(main_url)
        # print(type(req_ob))

        # json method return json format
        # data into python dictionary data type.

        # result contains list of nested dictionaries
        result = req_ob.json()
        # print(type(result))

        print(" Result before parsing the json data :\n", result)

        print("\n After parsing : \n Realtime Currency Exchange Rate for",
            result["Realtime Currency Exchange Rate"]["2. From_Currency Name"], "to",
            result["Realtime Currency Exchange Rate"]["4. To_Currency Name"], "is",
            result["Realtime Currency Exchange Rate"]['5. Exchange Rate'], to_currency)
        
        currencytobeconverted=result["Realtime Currency Exchange Rate"]['5. Exchange Rate']
        int_value=float(self.currencyfromentry.get())
        self.currencytoentry.insert(15,int_value*float(currencytobeconverted))

# Function to clear the values
    def clear(self):
        self.currencyfromentry.delete(0, "end")
        self.currencytoentry.delete(0, "end")


# currencyfrom = tk.Spinbox(root, fg="blue", width=6,font=12,values=("INR","USD","NPR","AUD")).grid(row=0,
# column=2)
# currencyto = tk.Spinbox(root, fg="blue", width=6,font=12,values=("INR","USD","NPR","AUD")).grid(
# row=1, column=2) spin box was quite not applicable in this case

def run():
    root = Tk()
    currency_converter_gui = Currency_converter(root)
    root.mainloop()

if __name__ == "__main__":
    run()
    


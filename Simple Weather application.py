# Real time weather application made from reference using geeksforgeeks
import tkinter as tk
from tkinter import messagebox

# import all functions from the tkinter

window = tk.Tk()

# function to find weather details
# of any city using openweathermap api
def tell_weather():
    # required modules
    import requests

    # enter your api key here
    api_key = "cf6a97df930dbaeb499ba5ed2c6c8b10"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # take a city name from city_field entry box
    city_name = citynameentry.get()
    clear()
    # complete_url variable to store complete url address
    complete_url = base_url + "q=" + city_name + "&APPID=" + api_key
    # "http://api.openweathermap.org/data/2.5/weather?q=Kathmandu&APPID=cf6a97df930dbaeb499ba5ed2c6c8b10"
    try:
        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        # json method of response object convert
        # json format data into python format data
        x = response.json()
        # now x contains list of  nested dictionaries
        # we know dictionary contains key value pair
        # check the value of "cod" key is equal to "404"
        # or not if not that means city is found
        # otherwise city is not found
        if x["cod"] != "404":
            # store the value of "main" key in variable y
            y = x["main"]
            # store the value corresponding to the "temp" key of y
            current_temperature = y["temp"]
            # store the value corresponding to the "pressure" key of y
            current_pressure = y["pressure"]
            # store the value corresponding to the "humidity" key of y
            current_humidity = y["humidity"]
            # store the value corresponding to the "temp_min" key of y
            min_temp = y["temp_min"]
            # store the value corresponding to the "temp_max" key of y
            max_temp = y["temp_max"]
            # store the value corresponding to the "dt" key of y
            wind_speed = x["dt"]
            # store the value of "weather" key in variable z
            z = x["weather"]
            # store the value corresponding to the "description" key
            # at the 0th index of z
            weather_description = z[0]["description"]
            # insert method inserting the
            # value in the text entry box.
            temperatureentry.insert(15, str(current_temperature) + " Kelvin")
            atmpressureentry.insert(15, str(current_pressure) + " hPa")
            humidityentry.insert(15, str(current_humidity) + " %")
            descriptionentry.insert(15, str(weather_description))
            windspeedentry.insert(15, str(wind_speed) + " m/s")
            mintemperatureentry.insert(15, str(min_temp) + " F")
            maxtemperatureentry.insert(15, str(max_temp) + " F")
            # messagebox.showinfo("hello",weather_description)

        # if city is not found
        else:
            # message dialog box appear which
            # shows given Error meassgae
            messagebox.showwarning("Warning", "   City not found\n""Please enter valid city name")
    except:
        messagebox.showerror("Error", "Some error occurred")
        citynameentry.delete(0, "end")


def clear():
    temperatureentry.delete(0, "end")
    atmpressureentry.delete(0, "end")
    humidityentry.delete(0, "end")
    descriptionentry.delete(0, "end")
    windspeedentry.delete(0, "end")
    mintemperatureentry.delete(0, "end")
    maxtemperatureentry.delete(0, "end")
    # code to delete the value from entry field
    citynameentry.focus_set()


v = tk.StringVar()

headlabel = tk.Label(window, text="Weather Application").grid(row=0, column=2)

cityname = tk.Label(window, text="City Name: ").grid(row=1, column=1)
citynameentry = tk.Entry(window)  # 1
citynameentry.grid(row=1, column=2, ipadx="90")  # 2
# ipadx for the width of the entry input_field
# to understand why #1 and #2 are spitted into two lines, go to this link
# https://stackoverflow.com/questions/1101750/tkinter-attributeerror-nonetype-object-has-no-attribute-attribute-name

submitbutton = tk.Button(window, text="Submit", bg="orange", command=tell_weather).grid(column=2, row=2)

temperature = tk.Label(window, text="Temperature: ").grid(row=3, column=1)
temperatureentry = tk.Entry(window)
temperatureentry.grid(row=3, column=2, ipadx="90")

atmpressure = tk.Label(window, text="atm pressure: ").grid(row=4, column=1)
atmpressureentry = tk.Entry(window)
atmpressureentry.grid(row=4, column=2, ipadx="90")

humidity = tk.Label(window, text="humidity: ").grid(row=5, column=1)
humidityentry = tk.Entry(window)
humidityentry.grid(row=5, column=2, ipadx="90")

description = tk.Label(window, text="description: ").grid(row=6, column=1)
descriptionentry = tk.Entry(window)
descriptionentry.grid(row=6, column=2, ipadx="90")

windspeed = tk.Label(window, text="Wind Speed: ").grid(row=7, column=1)
windspeedentry = tk.Entry(window)
windspeedentry.grid(row=7, column=2, ipadx="90")

mintemp = tk.Label(window, text="Min Temperature: ").grid(row=8, column=1)
mintemperatureentry = tk.Entry(window)
mintemperatureentry.grid(row=8, column=2, ipadx="90")

maxtemp = tk.Label(window, text="Min Temperature: ").grid(row=9, column=1)
maxtemperatureentry = tk.Entry(window)
maxtemperatureentry.grid(row=9, column=2, ipadx="90")

window.title("Weather Applicaiton")
window.geometry("450x250")
window.resizable(0, 0)

if __name__ == '__main__':
    tk.mainloop()

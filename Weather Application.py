import tkinter as tk
from tkinter import *
from tkinter import Entry
from tkinter import messagebox

window = tk.Tk()

def tell_weather():
    # required modules
    import requests, json
    api_key = "cf6a97df930dbaeb499ba5ed2c6c8b10"
    base_url= "http://api.openweathermap.org/data/2.5/weather?"
    city_name = citynameentry.get()
    clear()
     # complete_url variable to store complete url address
    complete_url = base_url + "q=" + city_name +"&APPID=" + api_key
    #"http://api.openweathermap.org/data/2.5/weather?q=Kathmandu&APPID=cf6a97df930dbaeb499ba5ed2c6c8b10"
    try:
        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        # json method of response object convert
        # json format data into python format data
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature= y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

         # store the value of "weather" key in variable z
            z= x["weather"]
            weather_description= z[0]["description"]
            temperatureentry.insert(15, str(current_temperature)+"Kelvin")
            atmpressureentry.insert(15, str(current_pressure)+"hPa")
            humidityentry.insert(15, str(current_humidity)+"%")
            descriptionentry.insert(15, str(weather_description))
            #messagebox.showinfo("hello",weather_description)
        else:
            messagebox.showwarning("Warning","   City not found\n"
            "Please enter valid city name")
    except:
        messagebox.showerror("Error","Some error occurred")
        citynameentry.delete(0,"end")


def clear():
    #citynameentry.delete(0, "end")
    temperatureentry.delete(0, "end")
    atmpressureentry.delete(0, "end")
    humidityentry.delete(0, "end")
    descriptionentry.delete(0, "end")
    #messagebox.showinfo("Success","Entry Field cleared successfully")
    #citynameentry.focus_set()


v = tk.StringVar()

headlabel = tk.Label(window, text="Weather Application").grid(row=0, column=2)

cityname = tk.Label(window, text="City Name: ").grid(row=1, column=1)
citynameentry = tk.Entry(window)#1
citynameentry.grid(row=1, column=2, ipadx="90")#2
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

window.title("Weather Applicaiton")
window.geometry("425x175")
window.resizable(0, 0)

if __name__ == '__main__':
    tk.mainloop()

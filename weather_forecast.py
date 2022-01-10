import tkinter as tk
from tkinter import ttk
from tkinter import *
import requests
import json

app = Tk()
app.title("Weather Forecast by Fayaz")
app.geometry("1200x400")

#API-KEY for the weather forecast
apiKey = "e98bf8f8a25327a2989e51f84031e90a"


baseURL = "http://api.openweathermap.org/data/2.5/weather?q="

# Get the city name from the user
city = input("Enter the name of the city: ")
completeURL = baseURL + city + "&appid=" + apiKey
response = requests.get(completeURL)
data = response.json()

#weather data
weather = data["weather"][0]["main"]
country = data["sys"]["country"]
icon = data["weather"][0]["icon"]
# conversion of temperature from Kelvin to Celcius
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15

high = data["main"]["temp_max"]
low = data["main"]["temp_min"]

high_temp = high - 273.15
low_temp = low - 273.15



heading = Label(app, text=f"{city}", font=("Montserrat", 20, "bold"), fg="Black")
heading.pack()

forecast = Label(app, text=f"{round(temp_celsius, 1)}°C", font=(
    "Montserrat", 30, "bold"), fg="Black")
forecast.pack()
condition = Label(app, text=f"{weather}", font=(
    "Montserrat", 24, "bold"), fg="Black")
condition.pack()
my_label = Label(app, text=f"It's currently {weather} in {city}, {country}. The current temperature in {city} is {round(temp_celsius, 1)}°C with a high of {round(high_temp, 1)}°C and a low of {round(low_temp, 1)}°C", font=(
    "Montserrat", 16), fg="black")

my_label.pack()
app.mainloop()

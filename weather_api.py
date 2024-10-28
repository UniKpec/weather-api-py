import requests
from tkinter import *
from tkinter import ttk
import datetime


#Api of Weather
weather_api_url ="https://api.open-meteo.com/v1/forecast?latitude=41.0138&longitude=28.9497&current=temperature_2m&hourly=temperature_2m&timezone=auto"
weather_api_response = requests.get(weather_api_url)
weather_api_json= weather_api_response.json()


#Window
weather_api = Tk()
weather_api.title("WEATHER API")
weather_api.minsize(width=500,height=500)


#define a grid
weather_api.columnconfigure((0,2,3),weight=3)
weather_api.columnconfigure(1,weight=5)
weather_api.rowconfigure((0),weight=5)
weather_api.rowconfigure((1,2,3),weight=3)


#Labels and some attributes
city = weather_api_json["timezone"]
city = city.split("/")
time =  weather_api_json["current"]["time"]
time = time.split("T")


instant_time = datetime.datetime.now()
hour = instant_time.strftime("%H")
minu = instant_time.strftime("%M")


weather_api_title = ttk.Label(weather_api,text=city[1],font=("Helvetica", "18", "bold"))
weather_api_temperature = ttk.Label(weather_api,text=f"{city[1]} City Temperature(°C)",font=("Helvetica","14"))
weather_api_temperature_number = ttk.Label(weather_api,text=weather_api_json["current"]["temperature_2m"],font=("Helvetica","14"))
weather_api_time = ttk.Label(weather_api,text="Time and Date",font=("Helvetica","14"))
weather_api_time_number = ttk.Label(weather_api,text=time[0]+"-"+time[1],font=("Helvetivca","14"))
weather_api_instant_time = ttk.Label(weather_api,text=f"{hour}:{minu}",font=("Helvetica","12"))


#Place a widget
weather_api_title.grid(row=0,column=1,sticky="e")
weather_api_temperature.grid(row=1,column=1,sticky="nw")
weather_api_temperature_number.grid(row=1,column=2,sticky="n")
weather_api_time.grid(row=2,column=1,sticky="nw")
weather_api_time_number.grid(row=2,column=2,sticky="n")
weather_api_instant_time.grid(row=3,column=2,sticky="se")



#run
weather_api.mainloop()
# importing modules

from tkinter import *
import requests
import json
import tkinter.messagebox as thh

root = Tk()
root.geometry("855x644")
root.minsize(855,644)
root.maxsize(855,644)
root.title("Weather-Feather---By Aryan Tiwari")
root.config(bg="#0f4c81", cursor="target")
root.iconbitmap("resource/sun.ico")



def weather():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "Your API Key Here"
    complete_url = base_url + "appid=" + api_key + "&q=" + entry.get()
    respons = requests.get(complete_url)
    x = respons.json()
    print (x)
    if x["cod"] != "404" : 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        label.insert(15, str(current_temperature) + " Kelvin") 
        label2.insert(10, str(current_pressure) + " hPa") 
        label3.insert(15, str(current_humidiy) + " %") 
        label4.insert(10, str(weather_description) )         


    else : 
  
        thh.showerror("Error", "City Not Found \n"
                        "Please enter valid city name") 



label = Label(root,text="Your City Here" ,font="Helvetica 20 bold", fg="Yellow", bg="#0f4c81")
label.pack(pady=20)

entry = Entry(root, font="lucida 20 bold", textvariable="city")
entry.pack()


button = Button(root, text="Submit Now", font="time 18 bold", fg="blue", bg="pink", command=weather)
button.pack(pady=30)

current_temperature = Label(root, text="Current Tempreture", font ="Helvetica 20 bold",bg = "#0f4c81", fg="yellow" )
current_temperature.pack(pady=5)


label = Entry(root, font="time 18 bold" )
label.pack()

current_pressure = Label(root, text="Current Pressure", font ="Helvetica 20 bold",bg = "#0f4c81", fg="yellow" )
current_pressure.pack(pady=5)

label2 = Entry(root,  font="time 18 bold" )
label2.pack()

current_humidity = Label(root, text="Current Humidity", font ="Helvetica 20 bold",bg = "#0f4c81", fg="yellow")
current_humidity.pack(pady=5)

label3 = Entry(root, font="time 18 bold" )
label3.pack()

Description = Label(root, text="Description", font ="Helvetica 20 bold",bg = "#0f4c81", fg="yellow" )
Description.pack(pady=5)


label4 = Entry(root , font="time 18 bold" )
label4.pack()


root.mainloop()
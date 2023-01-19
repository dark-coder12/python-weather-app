import configparser
import json
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

key = '26fa5915900fc421a1280da20430e47a'

def searchCity(c_):
    
    weatherInfo = requests.get(url.format(c_, key))
    
    if weatherInfo:
        jsonFormat = weatherInfo.json()
        c = jsonFormat['name']
        country = jsonFormat['sys']['country']
        temp = jsonFormat['main']['temp'] - 273.15
        tempF = temp *9/5 + 32;
        icon = jsonFormat['weather'][0]['icon']
        weat = jsonFormat['weather'][0]['main']
        final  = (c, country, temp, tempF, icon, weat)
        print(final)
        return final
    else:
        return None


def W():
  
    searched = city.get()
    info = searchCity(searched)
    print(info)
    if info is not None:
        cityInfo['text'] = '{} , {}'.format(info[0], info[1])
        tempurature['text'] = '{:2f} C , {:2f} F'.format(info[2], info[3])
        img['file'] = '{:3}@2x.png'.format(info[4])
    else:
        messagebox.showerror("City wasn't found!")
weather = Tk()
weather.title('Quick Weather!')

weather.geometry('500x400')
weather.config(bg = "white")

city = StringVar()

Label(weather, text = "Quick Weather", bg = "white", fg = "black", font = ("Calibri bold", 15), pady = 15).pack()

inputField = Entry(weather, textvariable = city, bg = "white")
inputField.pack(pady = 5)

searchedVal = Button(weather, width = 6, text = "Go!", bg = "white", fg = "black", command = W)
searchedVal.pack(pady= 5)

tempurature = Label(weather, text = '') 
tempurature.pack(pady = 5)

cityInfo = Label(weather, font = ("Calibri bold", 15), text = '')
cityInfo.pack()

img = PhotoImage(file = '')
button = Button(weather, image=img)
button.pack()

  
weather.mainloop()

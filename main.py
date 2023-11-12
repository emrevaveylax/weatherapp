from tkinter import *
import requests
from PIL import ImageTk,Image

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = '55018451666e7f45c41e10c573f6e99c'
iconUrl = 'https://openweathermap.org/img/wn/{}@2x.png'

def getWearher(city):
    params = {'q':city,'appid':api_key,'lang':'tr'}
    data = requests.get(url,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return (city,country,temp,icon,condition)

def main():
    city= cittyEntry.get()
    weather = getWearher(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{}°C'.format(weather[2])
        conditionaLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]),stream=True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon

app = Tk()
app.geometry('300x450')
app.title('Hava Durumu')

cittyEntry = Entry(app,justify='center')
cittyEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cittyEntry.focus()

searchButton = Button(app,text='Arama',font=('Arial',15),command=main)
searchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app,font=('Arial',40))
locationLabel.pack()

tempLabel = Label(app,font=('Arial',50,'bold'))
tempLabel.pack()

conditionaLabel = Label(app,font=('Arial',20))
conditionaLabel.pack()

app.mainloop()



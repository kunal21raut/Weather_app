import requests
from django.shortcuts import render,HttpResponse
from .models import CityData
from .forms import CityForm
import urllib.request
import json
# Create your views here.
def home(request):
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=34094488574bc04782fe5dd3b4efa4e8'

    if request.method == 'POST':

        city = request.POST['cityname']
        url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=f180fc8702526934bfc3e5c157777d62').read()

        list_of_data = json.loads(url)
        city_weather = {
            "country_code": str(list_of_data['sys']['country']),
            "temp":str(round((list_of_data['main']['temp'] - 272.15),2))+ ' °C',
            "temp_min":str(round((list_of_data['main']['temp_min'] - 272.15),2))+ ' °C',
            "temp_max":str(round((list_of_data['main']['temp_max'] - 272.15),2))+ ' °C',

            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
            "icon":list_of_data['weather'][0]['icon'],
            "description":str(list_of_data['weather'][0]['description']),
            "city":city,

        }
        print(city_weather)
    else:
        city_weather = {}


    return render(request,'weather_app/index.html',city_weather)

def about(request):
    return HttpResponse("<h2>About Page</h2>")
 
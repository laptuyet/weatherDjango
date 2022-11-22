from django.shortcuts import render
import urllib.request
import json


# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city'].split(',')[0]
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' 
        + city + '&units=metric&lang=en&appid=53c8e7ab7f6a20fa88273cec40ed2b32').read()
        dataList = json.loads(source)
        data=  {
             "country_code": str(dataList['sys']['country']),
            "coordinate": str(dataList['coord']['lon']) + ', '
            + str(dataList['coord']['lat']),

            "temp": str(dataList['main']['temp']) + ' °C',
            "pressure": str(dataList['main']['pressure']),
            "humidity": str(dataList['main']['humidity']),
            'main': str(dataList['weather'][0]['main']),
            'description': str(dataList['weather'][0]['description']),
            'icon': dataList['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
from django.shortcuts import render
import requests
import datetime


# Create your views here.
def index(request):
    message = 'PLease, Choose lat and long First to show your city weather.'
    if request.method == 'POST':
        if 'lat' in request.POST:
            lat = request.POST['lat']
        if 'lon' in request.POST:
            lon = request.POST['lon']
        
        message = 'incorrect lat and lon are given'

    try:
        appid = 'd20315e4ab814d0cb2575445a98a674c'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PARAMS = {'lat': lat, 'lon': lon, 'appid': appid, 'units': 'metric'}
        r = requests.get(url=URL, params=PARAMS)
        res = r.json()
        context = {
            'weathers': res['weather'],
            'name': res['name'],
            'date': datetime.date.today()
        }
        return render(request, 'weather_app/index.html', context)
    except:
        return render(request, 'weather_app/index.html', {'message': message})

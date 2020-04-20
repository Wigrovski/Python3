import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = 'bcbf096765e3208ebf85abeaf83b15c7'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    err_msg = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            city_count = City.objects.filter(name=new_city).count()
            if city_count == 0:
                r = requests.get(url.format(new_city)).json()
                print(r)
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'Нет такого города'
            else:
                err_msg = 'Город уже в списке '


    print(err_msg)
    form = CityForm()


    cities = City.objects.all()
    all_cities = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()


        city_info = {
            'city': city.name,
            'temp': r['main']['temp'],
            'icon': r['weather'][0]['icon'],
        }
        all_cities.append(city_info)
    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)


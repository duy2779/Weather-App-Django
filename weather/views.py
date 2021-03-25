from django.shortcuts import render, redirect
import requests
from .forms import CityForm
from .models import City
from django.contrib import messages

# Create your views here.
def home_view(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=169416a960ee036d3824e808b93cd7d9'

    form = CityForm(request.POST or None)
    if form.is_valid():
        add_city(request, form, url)

    cities = City.objects.all()
    cities_weather = []

    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'].capitalize(),
                'icon': r['weather'][0]['icon']
            }
        cities_weather.append(city_weather)
    context = {'form':form, 'cities_weather':cities_weather}

    return render(request, 'weather/weather.html', context)


def add_city(request, form, url):
    city = form.cleaned_data.get('name')
    r = requests.get(url.format(city)).json()
    #check city is exist
    if r['cod']=='404':
        messages.warning(request, 'City does not exist')
    else:
        form.save()
        messages.success(request, 'That city was added successfully')


def city_remove(request, pk):
    city = City.objects.get(pk=pk)
    city.delete()
    messages.success(request, 'remove success')
    return redirect('weather:home')
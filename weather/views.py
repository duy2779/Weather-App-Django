from django.shortcuts import render
import requests

# Create your views here.
def home_view(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=169416a960ee036d3824e808b93cd7d9'

    city = 'Las Vegas'

    if request.method == 'POST':
        form = request.POST
        city=form['city']

    r = requests.get(url.format(city)).json()
    city_weather = {}

    if r['cod']=='404':
        print('city not exist')
    else:
        city_weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'].capitalize(),
                'icon': r['weather'][0]['icon']
            }
    context = {'city_weather':city_weather}

    return render(request, 'weather/weather.html', context)
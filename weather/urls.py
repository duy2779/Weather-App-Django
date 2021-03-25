from django.urls import path
from .views import home_view, city_remove

app_name = 'weather'

urlpatterns = [
    path('', home_view, name='home'),
    path('city-remove/<int:pk>/', city_remove, name='city-remove'),
]
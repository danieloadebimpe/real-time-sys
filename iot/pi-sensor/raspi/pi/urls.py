from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/', views.get_temp, name='temperature'),
    path('hum/', views.get_humidity, name='humidity'),
    path('pres', views.get_pressure, name='pressure')
]
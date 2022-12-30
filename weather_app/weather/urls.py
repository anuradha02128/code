from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_items, name='post_list'),
    path('add_Yld/', views.add_Yld, name='add_Yld'),
    path('api/weather/', views.weather_data, name='weather'),
    path('api/yield/', views.Yield_data, name='yield'),
]
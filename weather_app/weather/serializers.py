from django.db.models import fields
from rest_framework import serializers
from .models import *

# class WeatherSerializer(serializers.Serializer):
#     date = serializers.CharField(max_length=200)
#     max_temp = serializers.CharField(max_length=200)
#     min_temp = serializers.CharField(max_length=200)
#     amt_precipitation = serializers.CharField(max_length=200)

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('date', 'max_temp', 'min_temp', 'amt_precipitation')

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = ('year', 'tot_harvested', )
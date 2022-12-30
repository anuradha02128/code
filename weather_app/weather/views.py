from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import os
import pandas as pd
from django.db.models import Avg,Sum
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/Aman',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

def get_weather_data(path):
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['date', 'max_temp', 'min_temp', 'amt_precipitation'])


def get_crop_data(path):
    if os.path.isfile(path):
        return pd.read_csv(path, sep='\t', names=['year', 'tot_harvested'])



@api_view(['GET'])
def add_items(request):
    root_dir=os.path.dirname(os.path.realpath(__file__))
    path=root_dir+"\code-challenge-template-main\wx_data"
    data={}
    try:
        if os.path.exists(path):
            for file in os.listdir(path):
                # print("fff: ", file)
                p=os.path.join(path, file)
                df = get_weather_data(p)
                df['amt_precipitation'] = df['amt_precipitation'].fillna(0)
                df[['max_temp','min_temp']] = df[['max_temp','min_temp']].fillna('')
                df.drop_duplicates()
                df['date'] = pd.to_datetime(df['date'].astype(str), format='%Y%m%d')
                # df['date'] = pd.DatetimeIndex(df['date']).year
                df['year'] = pd.DatetimeIndex(df['date']).year
                # df = df.groupby('date').agg({'max_temp': ['mean'], 'min_temp': ['mean'], 'amt_precipitation': ['sum']})
                # print(df)
                db_value = df.to_dict(orient='records')
                for data in db_value:
                	print(data["year"], data["date"])
	                try:
	                	# Weather.objects.bulk_create([Weather(**i) for i in db_value]) #bulk insert in table
	                	Weather.objects.create(**data)
	                except Exception as e:
	                	continue
                
                data["msg"]="data Inserted"
    except Exception as e:
        raise e
        
    return Response(data)


@api_view(['GET'])
def add_Yld(request):
    root_dir=os.path.dirname(os.path.realpath(__file__))
    path=root_dir+"\code-challenge-template-main\yld_data"
    data={}
    try:
        if os.path.exists(path):
            for file in os.listdir(path):
                p=os.path.join(path, file)
                df = get_crop_data(p)
                df['tot_harvested'] = df['tot_harvested'].fillna(0)
                df[['year','tot_harvested']] = df[['year','tot_harvested']].fillna('')
                df.drop_duplicates()
                db_value = df.to_dict(orient='records')
                # Yield.objects.bulk_create([Yield(**i) for i in db_value]) #bulk insert in table
                for data in db_value:
	                try:
	                	Yield.objects.create(**data)
	                except Exception as e:
	                	continue
                data["msg"]="data Inserted"
    except Exception as e:
        raise e
        
    return Response(data)

    
@api_view(['GET'])
def weather_data(request):
    data={}
    qry="""SELECT id, year ,avg(max_temp) avg_max_temp, avg(min_temp) avg_min_temp, sum(amt_precipitation) sum_amt_precipitation FROM weather group by year"""
    try:
        obj=Weather.objects.raw(qry)
        data_list=[]
        for row in obj:
        	data=row.__dict__
        	del data['_state']
        	data_list.append(data)        
    except Exception as e:
        raise e
        
    return Response(data_list)


@api_view(['GET'])
def Yield_data(request):
    data={}    
    try:
        obj=Yield.objects.all()
        data_list=[]
        for row in obj:
        	data=row.__dict__
        	del data['_state']
        	data_list.append(data)        
               
    except Exception as e:
        raise e
        
    return Response(data_list)
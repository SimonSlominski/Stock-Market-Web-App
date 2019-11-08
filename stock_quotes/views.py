from django.shortcuts import render
from datetime import datetime
import requests
import json
import quandl



# Quandl: CDProject JSON data
def home(request):


    api_request = requests.get('https://www.quandl.com/api/v3/datasets/WSE/CDPROJEKT.json?api_key=MVsz3tSzW19rrW55qTXJ')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "API Error"

    return render(request, 'home.html', {'api': api})


# Tiingo: it's working and it's also in JSON. But there is no GPW Data
# def home(request):
#
#     token = '571456b7e09771458b5e1a77dc75cd72835b7890'
#     ticker = 'AAPL'
#     start_date = '2019-10-08'
#
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Token ' + token
#     }
#
#     api_request = requests.get('https://api.tiingo.com/tiingo/daily/' + ticker + '/prices?startDate=' + start_date,
#                                    headers=headers)
#
#     try:
#         api = json.loads(api_request.content)
#     except Exception as e:
#         api = "API Error"
#
#     return render(request, 'home.html', {'api': api})


# Quandl: it's working but type(df) == <class 'pandas.core.frame.DataFrame'>
# def home(request):
#
#     quandl.ApiConfig.api_key = 'MVsz3tSzW19rrW55qTXJ'
#     df = quandl.get('WSE/CDPROJEKT', start_date='2019-10-08', end_date='2019-11-08')
#
#     try:
#         api = df
#     except Exception as e:
#         api = "API Error"
#
#     return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
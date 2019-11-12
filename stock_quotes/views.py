from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StockTicker
from .forms import StockTickerForm
from datetime import datetime
import requests
import json
import quandl



# Quandl: CDProject JSON data
def home(request):

    if request.method == 'POST':
        token = 'MVsz3tSzW19rrW55qTXJ'
        ticker = request.POST['ticker']
        start_date = '2019-11-01'
        end_date = '2019-11-08'

        api_request = requests.get('https://www.quandl.com/api/v3/'
                                   'datasets/WSE/' + ticker + '.json?'
                                   'api_key='      + token + '&'
                                   'start_date='   + start_date + '&'
                                   'end_date='     + end_date)

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "API Error"
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': 'Enter company name...'})




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


def add_stock(request):
    if request.method == 'POST':
        form = StockTickerForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock ticker has been added.'))
            return redirect('add_stock')
    else:
        ticker = StockTicker.objects.all()

        output = []
        for ticker_item in ticker:
            token = 'MVsz3tSzW19rrW55qTXJ'

            start_date = '2019-11-08'
            end_date = '2019-11-08'

            api_request = requests.get('https://www.quandl.com/api/v3/'
                                       'datasets/WSE/' + str(ticker_item) + '.json?'                          
                                       'api_key=' + token + '&'
                                       'start_date=' + start_date + '&'
                                       'end_date=' + end_date)

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "API Error"

        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request, stock_id):
    item = StockTicker.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, (f'Company {item} has been deleted from your portfolio'))
    return redirect(add_stock)











'''The views.py file is used to form an interconnection between the Model and the template and to extract data with the use of an API key
and store it in the database to perform any sort of CRUD operation or Data Analysis as well.
'''
import requests
from django.shortcuts import render
from .models import ConversionHistory
from datetime import datetime, timedelta
from decouple import config

# API_KEY =  '' # Replace with your actual API key. 
API_KEY = config('API_KEY')

def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}" # If any other url is used for extraction make changes here.
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['conversion_rates'].get(to_currency)
    else:
        return None

def get_historical_data(from_currency, to_currency):
    historical_data = {}
    end_date = datetime.now()

    for i in range(5):
        date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/historical/{from_currency}/{date}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            historical_rate = data['conversion_rates'].get(to_currency)
            if historical_rate:
                historical_data[date] = historical_rate

    return historical_data

def convert_currency(from_currency, to_currency, amount):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        # Save the conversion to the database
        ConversionHistory.objects.create(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            converted_amount=converted_amount
        )
        return converted_amount, exchange_rate  # Return both converted amount and exchange rate
    else:
        return None, None  # Return None if there's an error

def get_conversion_history():
    return ConversionHistory.objects.all().order_by('-id')  # Fetch all records, most recent first

def index(request):
    conversion_result = None
    present_value = None
    historical_data = {}
    conversion_history = get_conversion_history()  # Fetch conversion history

    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        conversion_result, present_value = convert_currency(from_currency, to_currency, amount)
        historical_data = get_historical_data(from_currency, to_currency)  # Get historical data for selected conversion

    return render(request, 'converter/index.html', {
        'conversion_result': conversion_result,
        'present_value': present_value,  # Pass present value to the template
        'historical_data': historical_data,
        'conversion_history': conversion_history,  # Pass conversion history to the template
    })

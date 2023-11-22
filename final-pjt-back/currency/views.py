from django.shortcuts import render
from django.db.models import Max
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, datetime



# Create your views here.
@api_view(['GET'])
def exchange(request):
    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() -4
        today = today - datetime.timedelta(days=diff)
    today = today.strftime('%Y%m%d')
    api_key = settings.CUR_API_KEY

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20231117&data=AP01'

    response = requests.get(url).json()
    return Response(response)

@api_view(['POST'])
def to_kor(request):
    amount = float(request.data.get('amount'))
    selected_currency = request.data.get('selectedCurrency')

    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() -4
        today = today - datetime.timedelta(days=diff)
    today = today.strftime('%Y%m%d')
    api_key = settings.CUR_API_KEY

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20231117&data=AP01'

    response = requests.get(url).json()
    # return Response(response)
    kor_amount = None
    for rate in response:
        if rate['cur_unit'] == selected_currency:
            rate_str = rate['kftc_deal_bas_r'].replace(',', '')
            exchange_rate = float(rate_str)
            kor_amount = amount * exchange_rate
            break
    response_data = {'converted_amount': kor_amount}
    return JsonResponse(response_data)


@api_view(['POST'])
def kor_to(request):
    amount = float(request.data.get('korAmount'))
    selected_currency = request.data.get('selectedCurrencyKor')

    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() -4
        today = today - datetime.timedelta(days=diff)
    today = today.strftime('%Y%m%d')
    api_key = settings.CUR_API_KEY

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key}&searchdate=20231117&data=AP01'

    response = requests.get(url).json()

    exchange_rate = None
    for rate in response:
        if rate['cur_unit'] == selected_currency:
            rate_str = rate['kftc_deal_bas_r'].replace(',', '')
            exchange_rate = float(rate_str)
            converted_amount = amount / exchange_rate
            break
    response_data = {'converted_amount': converted_amount}

    return JsonResponse(response_data)
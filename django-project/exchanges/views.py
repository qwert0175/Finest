from django.shortcuts import render
from datetime import datetime
from django.utils.dateformat import DateFormat
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExchangeSerializer
from .models import Exchange
import requests

# Create your views here.
@api_view(['GET', 'POST'])
def getExchangeInfo(request):
    if request.method == 'GET':
        exchange_info = Exchange.objects.all()
        serializer = ExchangeSerializer(data=exchange_info, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'POST':
        today = DateFormat(datetime.now()).format('Ymd')
        API_KEY = 'ILRkFGOHTVonQF47rmDk9ApE36iifjCw'
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={today}&data=AP01'
        response = requests.get(url)
        datas = response.json()
        for data in datas:
            data['deal_bas_r'] = float(data['deal_bas_r'].replace(',',''))
        serializer = ExchangeSerializer(data=datas, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
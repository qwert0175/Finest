from django.shortcuts import render
from datetime import datetime, timedelta
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
        for i in range(7):
            today = datetime.now() - timedelta(i)
            API_KEY = 'ILRkFGOHTVonQF47rmDk9ApE36iifjCw'
            url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={DateFormat(today).format('Ymd')}&data=AP01'
            response = requests.get(url)
            datas = response.json()
            if datas != []:
                break
        if datas == []:
            return Response({'message': '데이터가 존재하지 않습니다.'})
        for data in datas:
            data['deal_bas_r'] = float(data['deal_bas_r'].replace(',',''))
            if '(100)' in data['cur_unit']:
                data['cur_unit'] = data['cur_unit'].replace('(100)','')
                data['deal_bas_r'] = data['deal_bas_r'] / 100
        serializer = ExchangeSerializer(data=datas, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
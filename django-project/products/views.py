from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan, CreditLoanOptions
from .serializers import DepositSerializer, DepositOptionsSerializer, SavingSerializer, SavingOptionsSerializer, CreditLoanSerializer, CreditLoanOptionsSerializer
import requests

# Create your views here.
@api_view(['GET', 'POST'])
def getProductsInfo(request):
    if request.method == 'GET':
        return Response('good')
    elif request.method == 'POST':
        API_KEY = '40aba2698edb26d1e441c72a37a81982'
        deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
        saving_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
        creditloan_url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={API_KEY}&topFinGrpNo=050000&pageNo=1'
        deposit_response = requests.get(deposit_url)
        deposit_data = deposit_response.json()
        saving_response = requests.get(saving_url)
        saving_data = saving_response.json()
        creditloan_response = requests.get(creditloan_url)
        creditloan_data = creditloan_response.json()

        deposit_serializer = DepositSerializer(data=deposit_data['result']['baseList'], many=True)
        if deposit_serializer.is_valid():
            deposit_serializer.save()
        else:
            return Response(deposit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        deposit_options_serializer = DepositOptionsSerializer(data=deposit_data['result']['optionList'], many=True)
        if deposit_options_serializer.is_valid():
            deposit_options_serializer.save()
        else:
            return Response(deposit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
        saving_serializer = SavingSerializer(data=saving_data['result']['baseList'], many=True)
        if saving_serializer.is_valid():
            saving_serializer.save()
        else:
            return Response(saving_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
        saving_options_serializer = SavingOptionsSerializer(data=saving_data['result']['optionList'], many=True)
        if saving_options_serializer.is_valid():
            saving_options_serializer.save()
        else:
            return Response(saving_options_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        creditloan_serializer = CreditLoanSerializer(data=creditloan_data['result']['baseList'], many=True)
        if creditloan_serializer.is_valid():
            creditloan_serializer.save()
        else:
            return Response(creditloan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        creditloan_options_serializer = CreditLoanOptionsSerializer(data=creditloan_data['result']['optionList'], many=True)
        if creditloan_options_serializer.is_valid():
            creditloan_options_serializer.save()
        else:
            return Response(creditloan_options_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response('성공적으로 저장되었습니다.', status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan, CreditLoanOptions
from .serializers import DepositSerializer, DepositOptionsSerializer, SavingSerializer, SavingOptionsSerializer, CreditLoanSerializer, CreditLoanOptionsSerializer
import requests

# Create your views here.
@api_view(['POST'])
def getProductsInfo(request):
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
        return Response(deposit_options_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

@api_view(['GET'])
def getDeposits(request):
    deposits = Deposit.objects.all()
    deposit_options = DepositOptions.objects.all()
    deposits_serializer = DepositSerializer(deposits, many=True)
    deposit_options_serializer = DepositOptionsSerializer(deposit_options, many=True)
    return Response({
        "deposits": deposits_serializer.data,
        "deposit_options": deposit_options_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getSavings(request):
    savings = Saving.objects.all()
    saving_options = SavingOptions.objects.all()
    savings_serializer = SavingSerializer(savings, many=True)
    saving_options_serializer = SavingOptionsSerializer(saving_options, many=True)
    return Response({
        "savings": savings_serializer.data,
        "saving_options": saving_options_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getCreditLoans(request):
    creditloans = CreditLoan.objects.all()
    creditloan_options = CreditLoanOptions.objects.all()
    creditloans_serializer = CreditLoanSerializer(creditloans, many=True)
    creditloan_options_serializer = CreditLoanOptionsSerializer(creditloan_options, many=True)
    return Response({
        "creditloans": creditloans_serializer.data,
        "creditloan_options": creditloan_options_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getDepositOne(request, fin_cd):
    deposit = Deposit.objects.get(fin_prdt_cd=fin_cd)
    deposit_option = DepositOptions.objects.filter(fin_prdt_cd=fin_cd)
    deposit_serializer = DepositSerializer(deposit)
    deposit_option_serializer = DepositOptionsSerializer(deposit_option, many=True)
    return Response({
        "deposit": deposit_serializer.data,
        "deposit_options": deposit_option_serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def getSavingOne(request, fin_cd):
    saving = Saving.objects.get(fin_prdt_cd=fin_cd)
    saving_option = SavingOptions.objects.filter(fin_prdt_cd=fin_cd)
    saving_serializer = SavingSerializer(saving)
    saving_option_serializer = SavingOptionsSerializer(saving_option, many=True)
    return Response({
        "saving": saving_serializer.data,
        "saving_options": saving_option_serializer.data
    }, status=status.HTTP_200_OK)
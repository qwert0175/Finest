from rest_framework import serializers
from .models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan, CreditLoanOptions

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'
        
class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class CreditLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoan
        fields = '__all__'

class CreditLoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditLoanOptions
        fields = '__all__'
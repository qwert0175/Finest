from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    salary = models.IntegerField(null=True)
    asset = models.IntegerField(null=True)
    debt = models.IntegerField(null=True)
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, null=True)
    saving = models.ForeignKey(Saving, on_delete=models.CASCADE, null=True)
    # credit_loan = models.ForeignKey(CreditLoan, on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField(null=True)
    # period = models.CharField(max_length=20, null=True)
    # bank = models.CharField(max_length=20, null=True)

    
    # GENDER_CHOICES = [
    #     ("남성", "남성"),
    #     ("여성", "여성"),
    # ]

    # # ("모델명", "페이지 렌더링 문구")
    # PERIOD_CHOICE = [
    #     ("1년 이하", "1년 이하"),
    #     ("1년 초과 ~ 2년 이하", "1년 초과 ~ 2년 이하"),
    #     ("2년 초과 ~ 3년 이하", "2년 초과 ~ 3년 이하"),
    # ]

    # BANK_CHOICES = [
    #   ('우리은행','우리은행'),
    #   ('한국스탠다드차타드은행','한국스탠다드차타드은행'),
    #   ('대구은행','대구은행'),
    #   ('부산은행','부산은행'),
    #   ('광주은행','광주은행'),
    #   ('제주은행','제주은행'),
    #   ('전북은행','전북은행'),
    #   ('경남은행','경남은행'),
    #   ('중소기업은행','중소기업은행'),
    #   ('한국산업은행','한국산업은행'),
    #   ('국민은행','국민은행'),
    #   ('신한은행','신한은행'),
    #   ('농협은행','농협은행'),
    #   ('KEB하나은행','KEB하나은행'),
    #   ('수협은행','수협은행'),
    #   ('주식회사 카카오뱅크','주식회사 카카오뱅크'),
    #   ('주식회사 케이뱅크','주식회사 케이뱅크'),
    #   ('토스뱅크 주식회사','토스뱅크 주식회사'),
    #   ('기타','기타')
    # ]

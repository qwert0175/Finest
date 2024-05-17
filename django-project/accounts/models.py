from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
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
    #     ('우리은행','우리은행'),
    #     ('한국스탠다드차타드은행','한국스탠다드차타드은행'),
    #     ('대구은행','대구은행'),
    #     ('부산은행','부산은행'),
    #     ('광주은행','광주은행'),
    #     ('제주은행','제주은행'),
    #     ('전북은행','전북은행'),
    #     ('경남은행','경남은행'),
    #     ('중소기업은행','중소기업은행'),
    #     ('한국산업은행','한국산업은행'),
    #     ('국민은행','국민은행'),
    #     ('신한은행','신한은행'),
    #     ('농협은행','농협은행'),
    #     ('KEB하나은행','KEB하나은행'),
    #     ('수협은행','수협은행'),
    #     ('주식회사 카카오뱅크','주식회사 카카오뱅크'),
    #     ('주식회사 케이뱅크','주식회사 케이뱅크'),
    #     ('토스뱅크 주식회사','토스뱅크 주식회사'),
    #     ('기타','기타')
    # ]

    username = models.CharField(max_length=10, unique=True)
    nickname = models.CharField(max_length=10, null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True)
    salary = models.IntegerField(null=True)
    asset = models.IntegerField(null=True)
    debt = models.IntegerField(null=True)
    # deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    # saving = models.ForeignKey(Saving, on_delete=models.CASCADE)
    # period = models.CharField(max_length=20, choices=PERIOD_CHOICE, null=True)
    # bank = models.CharField(max_length=20, choices=BANK_CHOICES, null=True)

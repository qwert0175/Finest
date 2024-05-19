from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan


class User(AbstractUser):
    남성 = "남성"
    여성 = "여성"
    GENDER_CHOICES = [
        ("남성", "남성"),
        ("여성", "여성"),
    ]

    nickname = models.CharField(unique=True, max_length=10)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=2, choices=GENDER_CHOICES)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    asset = models.IntegerField(blank=True, null=True)
    debt = models.IntegerField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profile/')
    # deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, blank=True)
    # saving = models.ForeignKey(Saving, on_delete=models.CASCADE, blank=True)
    # credit_loan = models.ForeignKey(CreditLoan, on_delete=models.CASCADE, null=True)
    # is_staff = models.BooleanField(blank=True)
    # period = models.CharField(max_length=20, null=True)
    # bank = models.CharField(max_length=20, null=True)
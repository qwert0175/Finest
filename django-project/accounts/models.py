from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from products.models import Deposit, DepositOptions, Saving, SavingOptions, CreditLoan


class User(AbstractUser):
    nickname = models.CharField(unique=True, max_length=10)
    email = models.EmailField(blank=True, null=True)
    age = models.CharField(blank=False, null=False, max_length=2, validators=[MinLengthValidator(1)])
    birthday = models.CharField(blank=False, null=False, max_length=8, validators=[MinLengthValidator(8)])
    gender = models.CharField(blank=False, null=False, max_length=1, validators=[MinLengthValidator(1)])
    salary = models.CharField(blank=True, null=True, max_length=13)
    asset = models.CharField(blank=True, null=True, max_length=13)
    debt = models.CharField(blank=True, null=True, max_length=13)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profile/')
    # deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, blank=True)
    # saving = models.ForeignKey(Saving, on_delete=models.CASCADE, blank=True)
    # credit_loan = models.ForeignKey(CreditLoan, on_delete=models.CASCADE, null=True)
    # is_staff = models.BooleanField(blank=True)
    # period = models.CharField(max_length=20, null=True)
    # bank = models.CharField(max_length=20, null=True)
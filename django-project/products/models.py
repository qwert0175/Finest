from django.db import models

# Create your models here.
class Deposit(models.Model):
    fin_prdt_cd = models.CharField(max_length=30,primary_key=True)
    fin_prdt_nm = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=30)
    kor_co_nm = models.CharField(max_length=50)
    join_way = models.TextField()
    mtrt_int = models.CharField(max_length=200)
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.CharField(max_length=100)
    etc_note = models.TextField()
    max_limit = models.IntegerField(null=True)

class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(Deposit, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=30)
    intr_rate_type_nm = models.CharField(max_length=50)
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(max_length=10)
    intr_rate2 = models.FloatField(max_length=10)

class Saving(models.Model):
    fin_prdt_cd = models.CharField(max_length=30,primary_key=True)
    fin_prdt_nm = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=30)
    kor_co_nm = models.CharField(max_length=50)
    join_way = models.TextField()
    mtrt_int = models.CharField(max_length=200)
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.CharField(max_length=100)
    etc_note = models.TextField()
    max_limit = models.IntegerField(null=True)

class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(Saving, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=30)
    intr_rate_type_nm = models.CharField(max_length=50)
    rsrv_type = models.CharField(max_length=30)
    rsrv_type_nm = models.CharField(max_length=50)
    save_trm = models.IntegerField()
    intr_rate = models.FloatField(max_length=10)
    intr_rate2 = models.FloatField(max_length=10)

class CreditLoan(models.Model):
    fin_prdt_cd = models.CharField(max_length=30)
    fin_prdt_nm = models.CharField(max_length=50)
    fin_co_no = models.CharField(max_length=30)
    kor_co_nm = models.CharField(max_length=50)
    join_way = models.TextField()
    crdt_prdt_type = models.CharField(max_length=30)
    crdt_prdt_type_nm = models.CharField(max_length=50)
    cb_name = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fin_prdt_cd', 'fin_co_no'], name='unique_creditloan')
        ]

class CreditLoanOptions(models.Model):
    fin_prdt_cd = models.CharField(max_length=30)
    fin_co_no = models.CharField(max_length=30)
    crdt_lend_rate_type = models.CharField(max_length=30)
    crdt_lend_rate_type_nm = models.CharField(max_length=50)
    crdt_grad_1 = models.FloatField(max_length=10, null=True)
    crdt_grad_4 = models.FloatField(max_length=10, null=True)
    crdt_grad_5 = models.FloatField(max_length=10, null=True)
    crdt_grad_6 = models.FloatField(max_length=10, null=True)
    crdt_grad_10 = models.FloatField(max_length=10, null=True)
    crdt_grad_11 = models.FloatField(max_length=10, null=True)
    crdt_grad_12 = models.FloatField(max_length=10, null=True)
    crdt_grad_13 = models.FloatField(max_length=10, null=True)
    crdt_grad_avg = models.FloatField(max_length=10, null=True)
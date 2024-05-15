from django.db import models

# Create your models here.
class Exchange(models.Model):
    cur_unit = models.CharField(max_length=10,primary_key=True)
    cur_nm = models.CharField(max_length=20)
    deal_bas_r = models.FloatField(max_length=10)

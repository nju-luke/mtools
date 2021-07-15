from django.db import models
import datetime

# Create your models here.

class StockPrice(models.Model):
    username = models.CharField(max_length=32, default="nju_hyhb")
    # password = models.CharField(max_length=32)
    # age = models.IntegerField()
    code = models.CharField(primary_key = True,max_length=10)
    name = models.CharField(max_length=32)
    vi3 = models.IntegerField()
    vi2 = models.IntegerField()
    vi1 = models.IntegerField()
    v0 = models.IntegerField()
    vh1 = models.IntegerField()
    vh2 = models.IntegerField()
    vh3 = models.IntegerField()
    vcur = models.IntegerField()
    chg_date = models.CharField(max_length=32, default=datetime.datetime.today().strftime("%Y-%m-%d"))

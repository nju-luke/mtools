from django.db import models
import datetime

# Create your models here.

class StockPrice(models.Model):
    username = models.CharField(max_length=32, default="nju_hyhb")
    # password = models.CharField(max_length=32)
    # age = models.FloatField()
    code = models.CharField(primary_key = True,max_length=10)
    name = models.CharField(max_length=32)
    vi3 = models.FloatField()
    vi2 = models.FloatField()
    vi1 = models.FloatField()
    v0 = models.FloatField()
    vh1 = models.FloatField()
    vh2 = models.FloatField()
    vh3 = models.FloatField()
    vcur = models.FloatField()
    chg_date = models.CharField(max_length=32, default=datetime.datetime.today().strftime("%Y-%m-%d"))

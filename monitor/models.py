from django.db import models
import datetime

# Create your models here.

class StockPrice(models.Model):
    username = models.CharField(max_length=32, default="bianseyang")
    # password = models.CharField(max_length=32)
    # age = models.IntegerField()
    code = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=32)
    vi2 = models.IntegerField()
    vi1 = models.IntegerField()
    v0 = models.IntegerField()
    vh1 = models.IntegerField()
    vh2 = models.IntegerField()
    vcur = models.IntegerField()
    chg_date = models.CharField(max_length=32, default=datetime.datetime.today().strftime("%Y-%m-%d"))

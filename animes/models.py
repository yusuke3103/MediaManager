from django.db import models


# Create your models here.
class Title(models.Model):
    tid = models.CharField(max_length=4, primary_key=True)
    title = models.CharField(max_length=100)
    firstYear = models.CharField(max_length=4)
    firstMonth = models.CharField(max_length=2)
    firstEndYear = models.CharField(max_length=4, null=True)
    firstEndMonth = models.CharField(max_length=2, null=True)
    comment = models.CharField(max_length=5000, null=True)

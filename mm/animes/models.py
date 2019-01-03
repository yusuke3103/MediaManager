from django.db import models


# Create your models here.
class Title(models.Model):
    tid = models.CharField(max_length=4, blank=False, primary_key=True)
    title = models.CharField(max_length=100, blank=False)
    firstYear = models.CharField(max_length=4, blank=False)
    firstMonth = models.CharField(max_length=2, blank=False)
    firstEndYear = models.CharField(max_length=4, null=True)
    firstEndMonth = models.CharField(max_length=2, null=True)
    comment = models.CharField(max_length=5000, null=True)
    dirPath = models.FilePathField(null=True)

class SubTitle(models.Model):
    tid = models.CharField(max_length=4,blank=False)
    rno = models.CharField(max_length=3,blank=False)
    subtitle = models.CharField(max_length=100)
    
    class Meta:
        unique_together = (("tid","rno"))
from django.db import models

# Create your models here.

class Anime(models.Model):
	tid = models.CharField(blank=False, null=False, primary_key=True, max_length=4)
	title = models.CharField(blank=False, null=False, max_length=200)

	def __str__(self):
		return self.title
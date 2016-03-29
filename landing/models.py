from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Car(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	img = models.ImageField()

	def __str__(self):
		return self.title

class Rows_Number(models.Model):
	title = "Ilość wierszy"
	rows = models.IntegerField(default=0)

	def __str__(self):
		return self.title
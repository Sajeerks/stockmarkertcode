from django.db import models

# Create your models here.

class Address(models.Model):
	name = models.CharField(max_length = 100)
	email =  models.EmailField(max_length = 100)
	phone_number  =  models.CharField(max_length = 100)
	city  =  models.CharField(max_length = 100)
	state  =  models.CharField(max_length = 100)
	zipcode  =  models.IntegerField()

	def __str__(self):
		return self.name 

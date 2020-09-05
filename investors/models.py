from django.db import models
from accounts.models import User
# Create your models here.

class Investment(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	amount_invested=models.FloatField()
	date=models.DateTimeField(auto_now_add=True)
	dividend=models.FloatField( null=True, blank=True)
	product=models.CharField(max_length=200)
	product_2=models.CharField(max_length=200, null=True, blank=True)
	product_3=models.CharField(max_length=200, null=True, blank=True)
	product_4=models.CharField(max_length=200, null=True, blank=True)
	product_5=models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.user


from django.db import models
from accounts.models import User
from loans.models import Product, Category
# Create your models here.

class Investment(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	amount_invested=models.FloatField()
	date=models.DateTimeField(auto_now_add=True)
	dividend=models.FloatField( null=True, blank=True)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)

	# def __str__(self):
	# 	return self.user
		
class Payment(models.Model):
	investment=models.ForeignKey(Investment, on_delete=models.CASCADE)
	amount_paid=models.FloatField()
	date=models.DateTimeField(auto_now_add=True)
	# def __str__(self):
	# 	return self.investment



TIME_CHOICES = [
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
    ('Semi_Annualy', 'Semi_Annualy'),
    ('Annualy', 'Annualy'),
]
class Schema(models.Model):
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	benefit=models.IntegerField()
	date=models.DateTimeField(auto_now_add=True)
	time = models.CharField(
        max_length=50,
        choices=TIME_CHOICES,
        default='Monthly',
    )



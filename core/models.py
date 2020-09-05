from django.db import models
import datetime

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_USD = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return f'{self.enter_your_user_name} sent {self.enter_the_destination_account_number} a total of $ {self.enter_the_amount_to_be_transferred_in_USD} on {self.created_on}'
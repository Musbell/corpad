from django.db import models
import datetime
from accounts.models import User

class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

    def __str__(self):
        return self.user_name

class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_USD = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return f'{self.enter_your_user_name} sent {self.enter_the_destination_account_number} a total of $ {self.enter_the_amount_to_be_transferred_in_USD} on {self.created_on}'

class WalletHistory(models.Model):
    sender=models.CharField(max_length=200)
    receiver=models.CharField(max_length=200)
    amount=models.IntegerField()
    date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' Transaction Ticket Number ' +  str(self.pk)

class Withdraw(models.Model):
    email = models.CharField(max_length = 150, default = None)
    amount = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
]
class Announcement(models.Model):
	title=models.CharField(max_length=20)
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default='Low',
    )


class Notification(models.Model):
    target=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    # priority = models.CharField(
    #     max_length=50,
    #     choices=PRIORITY_CHOICES,
    #     default='Low',
    # )
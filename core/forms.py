from django import forms
from . import models

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "enter_your_user_name",
            "enter_the_destination_account_number", 
            "enter_the_amount_to_be_transferred_in_USD"
        ]


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model   =   models.Announcement
        fields  =   '__all__'


class NotificationForm(forms.ModelForm):
    class Meta:
        model   =   models.Notification
        fields  =   '__all__'

class WithdrawForm(forms.ModelForm):
    class Meta:
        model   =   models.Withdraw
        fields  =   [
            "email",
            "amount", 
        ]
    
class StatusForm(forms.ModelForm):
    class Meta:
        model   =   models.Status
        fields  =   '__all__'
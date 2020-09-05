from django import forms
from .models import *

class LoanForm(forms.ModelForm):
    commodity = forms.CharField(label='Commodity Name',widget=forms.TextInput(attrs={'placeholder': 'Which commodity do you want to loan?'}))
    installment = forms.CharField(label='Monthy Installment',widget=forms.TextInput(attrs={'placeholder': 'How much would you like to pay monthly?'}))
    months = forms.CharField(label='Total Months', widget=forms.TextInput(attrs={'placeholder': 'How long will it take you to clear the loan?'}))
    address = forms.CharField(label='Pickup Location', widget=forms.TextInput(attrs={'placeholder': 'Where are you located? Indicate a pickup location. '}))
    phone = forms.CharField(label='Valid Mobile',widget=forms.TextInput(attrs={'placeholder': 'How can we contact you?'}))
    # category= forms.ModelChoiceField(queryset=Category.objects.all(),
                                        # widget=forms.Select(attrs={'placeholder': 'Loan Category'}))
    # commodity = forms.ModelChoiceField(queryset=Product.objects.all(),)
    #                                     # widget=forms.TextInput())
    class Meta:
        model   =   Loan
        fields  =   ['commodity','installment', 'months', 'address','phone']
        # widgets = {
        #     'category': forms.ModelChoiceField(attrs={'class': 'form-control'}),
        # }
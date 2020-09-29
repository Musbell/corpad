from django import forms
from .models import *

class JoinForm(forms.ModelForm):
	class Meta:
		model   =   Join
		fields  =   ['category',]


class PaymentForm(forms.ModelForm):
	email=forms.EmailField(widget=forms.TextInput(attrs={
		'type':"email",
		'name':"email",
		'id':"email-address"
		}))

	amount=forms.IntegerField(widget=forms.TextInput(attrs={
		'type':"tel",
		'name':"amount",
		'id':"amount"
		}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={
		'type':"text",
		'name':"first-name",
		'id':"first-name"
		}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={
		'type':"text",
		'name':"last-name",
		'id':"last-name"
		}))
	class Meta:
		model   =   Payment
		fields  =   '__all__'

class CreateGroupForm(forms.ModelForm):
	# email=forms.EmailField(widget=forms.TextInput(attrs={
	# 	'type':"email",
	# 	'name':"email",
	# 	'id':"email-address"
	# 	}))

	# amount=forms.IntegerField(widget=forms.TextInput(attrs={
	# 	'type':"tel",
	# 	'name':"amount",
	# 	'id':"amount"
	# 	}))
	# first_name=forms.CharField(widget=forms.TextInput(attrs={
	# 	'type':"text",
	# 	'name':"first-name",
	# 	'id':"first-name"
	# 	}))
	# last_name=forms.CharField(widget=forms.TextInput(attrs={
	# 	'type':"text",
	# 	'name':"last-name",
	# 	'id':"last-name"
	# 	}))
	class Meta:
		model   =   AdashiGroup
		fields  =   '__all__'



class JoinUpdateForm(forms.ModelForm):
    class Meta:
        model   =   Join
        fields  =   ['approved',]
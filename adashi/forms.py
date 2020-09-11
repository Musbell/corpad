from django import forms
from .models import *

class JoinForm(forms.ModelForm):
	# members   =   forms.CharField()
	class Meta:
		model   =   Category
		fields  =   ['members',]
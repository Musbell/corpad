from django import template
from django.db.models import Count
from ..models import User
from core.models import *
from investors.models import *
from loans.models import *
from adashi.models import *

register = template.Library()


@register.simple_tag
def total_users():
	users=User.objects.all()
	return users.count()

@register.simple_tag
def total_groups():
	groups=AdashiGroup.objects.all()
	return groups.count()

@register.simple_tag
def total_investors():
	investors=Investment.objects.all()
	return investors.count()

@register.simple_tag
def total_loans():
	loans=Loan.objects.all()
	return loans.count()

@register.simple_tag
def total_staff():
	users=User.objects.all().filter(is_staff=True)
	return users.count()
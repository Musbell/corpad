from django import template
from django.db.models import Count
from ..models import User


register = template.Library()


@register.simple_tag
def total_users():
	users=User.objects.all()
	return users.count()

@register.simple_tag
def total_staff():
	users=User.objects.all().filter(is_staff=True)
	return users.count()
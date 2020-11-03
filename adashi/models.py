from django.db import models
from accounts.models import User
from django.urls import reverse
# Create your models here.

class AdashiGroup(models.Model):
	name=models.CharField(max_length=200, unique=True)
	num_of_members=models.IntegerField()# this holds the positions available in a group, I think this what you want? 
	cum_amount=models.IntegerField()
	contrib_amount=models.IntegerField()
	num_of_days_per_turn=models.IntegerField()
	group_id=models.IntegerField(unique=True)
	date=models.DateTimeField(auto_now_add=True)
	end_date=models.CharField(max_length=10)
	members=models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.name
	def get_absolute_url(sel):
		return reverse('adashi')

	@property
	def members_name(self):
		return [x.email for x in self.members]

class Position(models.Model):
	position_number=models.IntegerField()
	group=models.ForeignKey(AdashiGroup, on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

class Join(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='joins')
	category=models.ForeignKey(AdashiGroup, on_delete=models.CASCADE)
	spinned= models.BooleanField(default=False)
	approved=models.BooleanField(default=False)

	def __str__(self):
		return self.user.email


class Calendar(models.Model):
	category=models.ForeignKey(AdashiGroup, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendars')
	date=models.DateTimeField(auto_now_add=True)
	d_date=models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.user.email

class Payment(models.Model):
	email=models.EmailField()
	amount=models.IntegerField()
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)

	def __str__(self):
		return self.email




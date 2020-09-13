from django.db import models
from accounts.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	name=models.CharField(max_length=200, unique=True)
	num_of_members=models.IntegerField()
	cum_amount=models.IntegerField()
	contrib_amount=models.IntegerField()
	num_of_days_per_turn=models.IntegerField()
	group_id=models.IntegerField(unique=True)
	date=models.DateTimeField(auto_now_add=True)
	end_date=models.DateTimeField()
	members=models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.name
	def get_absolute_url(sel):
		return reverse('adashi')

	@property
	def members_name(self):
		return [x.email for x in self.members]


class Join(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='joins')
	category=models.ForeignKey(Category, on_delete=models.CASCADE)
	position=models.IntegerField(default=0)
	spinned=models.BooleanField(default=False)

	def __str__(self):
		return self.user.email
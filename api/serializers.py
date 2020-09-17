from rest_framework import serializers

from adashi.models import *

class JoinSerializer(serializers.ModelSerializer):
	class Meta:
		model=Join
		fields=('id','user', 'category', 'position','spinned')

	def create(self, validated_data):
	    return Join.objects.create(**validated_data)
	    """
	     Create and return a new `Join` instance, given the validated data.
	    """



class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model=Category
		fields=('id','name', 'num_of_members',)

	def create(self, validated_data):
	    return Category.objects.create(**validated_data)
	    """
	     Create and return a new `Join` instance, given the validated data.
	    """
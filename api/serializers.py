from rest_framework import serializers

from adashi.models import Join, Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'user', 'group', 'position_number']
    

    def create(self, validated_data):
        """
        Create and return a new `Join` instance, given the validated data.
        """
        return Position.objects.create(**validated_data)

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['id', 'user', 'category', 'spinned', 'approved']
    

    def create(self, validated_data):
        """
        Create and return a new `Join` instance, given the validated data.
        """
        return Join.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Join` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

# class JoinSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Join
# 		fields=('id','user', 'category', 'position','spinned')

# 	def create(self, validated_data):
# 	    return Join.objects.create(**validated_data)
# 	    """
# 	     Create and return a new `Join` instance, given the validated data.
# 	    """



# class CategorySerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Category
# 		fields=('id','name', 'num_of_members',)

# 	def create(self, validated_data):
# 	    return Category.objects.create(**validated_data)
# 	    """
# 	     Create and return a new `Join` instance, given the validated data.
# 	    """
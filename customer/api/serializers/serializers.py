from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=25)
    name=serializers.CharField(max_length=25)
    address=serializers.CharField(max_length=25)
    email=serializers.EmailField()
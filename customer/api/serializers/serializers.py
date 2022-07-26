from rest_framework import serializers
from customer.models import Customer
# class CustomerSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=25)
#     name=serializers.CharField(max_length=25)
#     address=serializers.CharField(max_length=25)
#     email=serializers.EmailField()


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields='__all__'

    # def to_representation(self, instance):
    #     return{
    #         "id":instance.id,
    #         "name":instance.name
    #     }
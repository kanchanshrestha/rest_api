from rest_framework import serializers
from customer.models import Customer
# class CustomerSerializer(serializers.Serializer):
#     username=serializers.CharField(max_length=25)
#     name=serializers.CharField(max_length=25)
#     address=serializers.CharField(max_length=25)
#     email=serializers.EmailField()


class CustomerDetailSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25,required=True,trim_whitespace=True)
    name=serializers.CharField(max_length=25,required=True,trim_whitespace=True)
    address=serializers.CharField(max_length=25,required=True,trim_whitespace=True)
    email=serializers.EmailField(required=True,trim_whitespace=True)

    class Meta:
        model=Customer
        fields='__all__'

class CustomerListSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return{
            "id":instance.id,
            "name":instance.name
        }
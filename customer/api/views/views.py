from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from customer.api.serializers.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def customer_details(request):
    customers=Customer.objects.all()
    serializer=CustomerSerializer(customers,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
    # return HttpResponse(json_data,content_type='application/json')
from customer.api.serializers.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def customer_details(request):
    customers=Customer.objects.filter(id=3)
    if customers:
        serializer=CustomerSerializer(customers)
        return Response({
            "status":True,
            "data":serializer.data
        })
    return Response({
            "status":False,
            "message":"User not found"
        },404)
    
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    # # return HttpResponse(json_data,content_type='application/json')

def details(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    if id:
        customer=Customer.objects.filter(id=id)
    if name:
        customer=Customer.objects.filter(name=name)
    else:
        customer=Customer.objects.all()






# def customer_details(request,id):
#     customers=Customer.objects.get(id=1)
#     serializer=CustomerSerializer(customers,many=True)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)
#     # return HttpResponse(json_data,content_type='application/json')
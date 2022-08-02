from customer.api.serializers.serializers import CustomerDetailSerializer
from customer.api.serializers.serializers import CustomerListSerializer
from customer.models import Customer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import View
# from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
# from rest_framework.views import APIView
# Create your views here.
# @api_view(['GET'])
# def customer(request):
#     customers=Customer.objects.all()
#     serializer=CustomerDetailSerializer(customers,many=True)
#     return Response({
#         "status":True,
#         "data":serializer.data
#     })
   
    
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    # # return HttpResponse(json_data,content_type='application/json')
@api_view(['GET'])
def customer_details(request):
    id=request.GET.get('id')
    name=request.GET.get('name')
    if id:
        customer=Customer.objects.filter(id=id)
    elif name:
        customer=Customer.objects.filter(name__icontains=name)
    else:
        customer=Customer.objects.all()
    serializer=CustomerDetailSerializer(customer,many=True)
    return Response({
        "status":True,
        "data":serializer.data
    })

# class MyView()

class Customer_List(generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class=CustomerListSerializer
    model=Customer
    def get(self, request):
        # used to get all the objects of the model, which is a good practice
        customers=self.model.objects.all() 
        # used to get the queryset only
        # customers=self.get_queryset() 
        serializer=self.get_serializer(customers,many=True)
        return Response({
            "status":True,
            "data":serializer.data
        })


class CreateCustomer(generics.GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerDetailSerializer
    model=Customer
    
    @api_view(['POST'])
    def create_customer(request):
        create_serializer=CustomerDetailSerializer(data=request.data)
        if create_serializer.is_valid():
            create_serializer.save()
            return Response({
                "status":True,
                "data":create_serializer.data,
                "message":"Customer Created Sucessfully"
            },201)
        else:
            return Response({
                "error":create_serializer.errors ,
                
                },422)

class UpdateCustomer(generics.GenericAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerDetailSerializer
    model=Customer
    
    @api_view(['PATCH'])
    def update_customer(request):
        customer=Customer.objects.get(id=14)
        update_serializer=CustomerDetailSerializer(data=request.data,instance=customer)
        # update_serializer=Customer.objects.filter(id=14).update(username=request.data.get["username"] )
        if update_serializer.is_valid():
            update_serializer.save()
            return Response({
                "status":True,
                "message":"Customer Detail Updated Sucessfully"
            })
        else:
            return Response({
                "error":update_serializer.errors ,
                
                },422)


# #MANUAL WAY
# class CreateCustomer(generics.GenericAPIView):
#     queryset=Customer.objects.all()
#     serializer_class=CustomerDetailSerializer
#     model=Customer
#     @api_view(['POST'])
#     def create_customer(request):
#         print(request.data)
#         customers=Customer.objects.create(username="karan2",name="Karan Shrestha",address="Kathmandu",email="karan@test.com")
#         return Response({
#             "status":True,
#             "message":"Customer Created Sucessfully"
#         })

# class UpdateCustomer(generics.GenericAPIView):
#     queryset= Customer.objects.all()
#     serializer_class=CustomerDetailSerializer
#     model=Customer

#     @api_view(['GET'])
#     def update_customer(request):
#         customers=Customer.objects.filter(id=14).update(address="North America,USA",email="taylor123@gmail.com")
#         return Response({
#             "status":True,
#             "message":"Customer Updated Sucessfully"
#         })

class DeleteCustomer(generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class=CustomerDetailSerializer
    model=Customer

    @api_view(['GET','DELETE'])
    def delete_customer(request):
        customers=Customer.objects.filter(id=21)
        # customers=Customer.objects.filter(id=4) 
        customers.delete()
        return Response({
            "status":True,
            "message":"Customer deleted Sucessfully"
        })

# API VIEW
# class DeleteCustomer(APIView):
#     queryset = Customer.objects.all()
#     serializer_class=CustomerSerializer
#     model=Customer
#     def delete(self,request):
#         customers=Customer.objects.get(id=2)
#         customers.delete()
#         return Response({
#             "status":204
#         })



# # Mixin Example but should not be used 
# class CreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset = Customer.objects.all
#     serializer_class=CustomerSerializer
#     def post(self, request):
#         return self.create(request)
    
# class MyView(mixins.UpdateModelMixin):
#     pass
# class MyView(mixins.RetrieveModelMixin):
#     pass
# class MyView(mixins.DestroyModelMixin):
#     pass

    

















# def customer_details(request,id):
#     customers=Customer.objects.get(id=1)
#     serializer=CustomerSerializer(customers,many=True)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)
#     # return HttpResponse(json_data,content_type='application/json')
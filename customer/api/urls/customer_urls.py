from django.urls import path, include
from customer.api.views.views import DeleteCustomer
from customer.api.views import views
from customer.api.views.views import Customer_List 
from customer.api.views.views import UpdateCustomer
from customer.api.views.views import CreateCustomer
urlpatterns = [
    path('customer/',views.customer_details,name="customer-details"),
    path('customer_details/',views.customer_details,name="details"),
    path('customer_list/',Customer_List.as_view(),name="customer_list"),
    path('deletecustomer/',DeleteCustomer.delete_customer,name="delete_customer"),
    path('update_customer/',UpdateCustomer.update_customer,name="update_customer"),
    path('create_customer/',CreateCustomer.create_customer,name="create_customer")
]

# url(r'^customer_details/(?id=1),views.customer_details,name="customer-details")
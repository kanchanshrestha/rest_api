from django.urls import path, include
from customer.api.views import views
urlpatterns = [
    path("customer_details/",views.customer_details,name="customer-details"),
    path("details/",views.details,name="details")
]

# url(r'^customer_details/(?id=1),views.customer_details,name="customer-details")
from django.contrib import admin

# Register your models here.
from customer.models import Customer

@admin.register(Customer)
class Customer(admin.ModelAdmin):
    pass
    list_display =("username","name","address","email")
from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'cash_price','installment_price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['cash_price','installment_price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['customer', 'commodity', 'installment','months',
                    'address', 'date', 'approved']
    list_filter = ['approved', 'date', 'customer']
    list_editable = ['commodity','address', 'approved']
    actions = ['approve_requests', ]

    def approve_requests(self, request, queryset):
        queryset.update(approved=True)
    approve_requests.short_description = "Mark selected requests as approved"



admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Loan)
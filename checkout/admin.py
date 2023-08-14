from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    # This class is used to display the line items in the admin panel
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    
class OrderAdmin(admin.ModelAdmin):
    # This class is used to display the order information in the admin panel
    inlines = (OrderLineItemAdminInline,)
    
    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total',)
    
    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'region', 'delivery_cost', 'order_total', 'grand_total',)
    
    list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost','grand_total',)
    
    ordering = ('-date',)
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem)
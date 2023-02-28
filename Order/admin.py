from django.contrib import admin
from . models import (Order,OrderItem,Payment,Coupon,Refund)
# Register your models here.


admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Refund)
from django.contrib import admin
from .models import GuestInfo, PaymentInfo

# Register your models here.

admin.site.register(GuestInfo)
admin.site.register(PaymentInfo)
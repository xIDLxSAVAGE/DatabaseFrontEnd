from django.contrib import admin
from .models import BbrAddress, BbrCustomer
from .models import UserProfile

# Register your models here.
admin.site.register(BbrAddress)
admin.site.register(BbrCustomer)

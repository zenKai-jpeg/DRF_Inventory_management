from django.contrib import admin
from .models import Inventory, Inbound, Outbound

admin.site.register(Inventory)
admin.site.register(Inbound)
admin.site.register(Outbound)
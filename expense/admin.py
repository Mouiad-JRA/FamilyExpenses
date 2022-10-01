from django.contrib import admin

# Register your models here.
from expense.models import Outlay, OutlayType, Material

admin.site.register(Material)
admin.site.register(OutlayType)
admin.site.register(Outlay)


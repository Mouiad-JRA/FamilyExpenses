from django.contrib import admin

from expense.models import Outlay, OutlayType, Material


class OutlayAdmin(admin.ModelAdmin):
    list_display = ('price', 'material', 'outlay_type', 'owner', 'date', 'date')
    search_fields = ('price', 'material', 'outlay_type', 'owner', 'date', 'date')
    list_per_page = 5


admin.site.register(Material)
admin.site.register(OutlayType)
admin.site.register(Outlay, OutlayAdmin)

from django.contrib import admin

# Register your models here.
from income.models import Income, Source

admin.site.register(Income)
admin.site.register(Source)


from django.contrib import admin
from .models import Property

# Register your models here.
class ProperytAdmin(admin.ModelAdmin):
    list_display = ('address', 'price')
    search_fields = ('address',)

admin.site.register(Property, ProperytAdmin)

from django.contrib import admin
from .models import Property

# Register your models here.
class ProperytAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

admin.site.register(Property, ProperytAdmin)

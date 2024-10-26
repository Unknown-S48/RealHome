# realtors/admin.py
from django.contrib import admin
from .models import Realtor, Contact

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'property__address')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
admin.site.register(Contact, ContactAdmin)


#coding: utf-8

from django.contrib import admin

from bitfield import BitField
from bitfield.forms import BitFieldCheckboxSelectMultiple

from .models import Filter, UserAdvert


class AdminFilter(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }
    list_display = ('id', 'user', 'is_rent', 'price_min', 'price_max', 'section',)
    list_filter = ('is_rent', 'section',)





class AdminUserAdvert(admin.ModelAdmin):
    list_display = ('id', 'filter', 'advert', 'is_read',)
    list_filter = ('is_read',)

admin.site.register(Filter, AdminFilter)
admin.site.register(UserAdvert, AdminUserAdvert)

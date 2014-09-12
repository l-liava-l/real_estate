from django.contrib import admin

from bitfield import BitField
from bitfield.forms import BitFieldCheckboxSelectMultiple

from .models import Advert


class AdminAdvert(admin.ModelAdmin):
    formfield_overrides = {
        BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }
    list_display = ('id', 'is_rent', 'price', 'section', 'cian_id',)
    list_filter = ('is_rent', 'section',)

admin.site.register(Advert, AdminAdvert)

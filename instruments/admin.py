from django.contrib import admin

# Register your models here.
from .models import Instrument, Variation

class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'exchange', 'symbol', 'multiplier']
    search_fields = ['title']
    list_filter = ['title']
    list_search = ['exhange']
    #list_editable=['']

    class Meta:
        model=Instrument




class VariationAdmin(admin.ModelAdmin):
    list_display=['__str__', 'instrument', 'active', 'symbol', 'multiplier']
    # list_editable=['inventory']

    class Meta:
        model=Variation

admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Variation, VariationAdmin)

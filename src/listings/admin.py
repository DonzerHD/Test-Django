from django.contrib import admin
from listings.models import Band, Listing

# Register your models here.
class BandAdmin (admin.ModelAdmin):
   list_display = ('id','name', 'genre', 'year_formed', 'active')

admin.site.register(Band, BandAdmin)

class ListingAdmin (admin.ModelAdmin):
   list_display = ('title', 'band')

admin.site.register(Listing, ListingAdmin)

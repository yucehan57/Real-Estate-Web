from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing_id', 'listing', 'name',
                    'email', 'user_id', 'contact_date')
    list_display_links = ('id', 'listing', 'email', 'user_id')
    list_filter = ('listing_id', 'user_id', 'listing', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

from django.contrib import admin
from .models import Banner, ContactInfo

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Banner instance
        if Banner.objects.exists():
            return False
        return True
    
admin.site.register(Banner, BannerAdmin)

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'address', 'facebook_link', 'twitter_link', 'linkedin_link')

    def has_add_permission(self, request):
        # Prevent adding more than one ContactInfo instance
        if ContactInfo.objects.exists():
            return False
        return True

admin.site.register(ContactInfo, ContactInfoAdmin)
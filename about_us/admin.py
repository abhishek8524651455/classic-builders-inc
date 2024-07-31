from django.contrib import admin
from about_us.models import Banner, CompanyProfile

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Banner instance
        if Banner.objects.exists():
            return False
        return True
    

admin.site.register(Banner, BannerAdmin)


class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Company Profile instance
        if CompanyProfile.objects.exists():
            return False
        return True
    

admin.site.register(CompanyProfile, CompanyProfileAdmin)


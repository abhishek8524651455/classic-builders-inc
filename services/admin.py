from django.contrib import admin
from django.db import models
from services.models import Banner, PostBannerContent, Services
# from .models import ServicePage, DetailedService
# from tinymce.widgets import TinyMCE

# Register your models here.



class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Banner instance
        if Banner.objects.exists():
            return False
        return True
    

admin.site.register(Banner, BannerAdmin)



class PostBannerContentAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Banner instance
        if PostBannerContent.objects.exists():
            return False
        return True

admin.site.register(PostBannerContent, PostBannerContentAdmin)
admin.site.register(Services)



# class ServicePageAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         # Prevent adding more than one ServicePage instance
#         if ServicePage.objects.exists():
#             return False
#         return True
#     list_display = ('meta_title', )

# admin.site.register(ServicePage, ServicePageAdmin)


# class DetailedServiceAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()},
#     }

#     list_display = ('meta_title', 'image_tag')
#     list_per_page = 50

# admin.site.register(DetailedService, DetailedServiceAdmin)

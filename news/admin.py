from django.contrib import admin
from news.models import Banner, News

# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('heading',)

    def has_add_permission(self, request):
        # Prevent adding more than one Banner instance
        if Banner.objects.exists():
            return False
        return True
    

admin.site.register(Banner, BannerAdmin)


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('heading', 'created_at')

admin.site.register(News)

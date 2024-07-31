from django.contrib import admin
from home.models import Banner, AboutUs, AboutServices, WhyUs, MainServices, SpecializedIn, SpecializedInServices, ProjectSectionTitle, Projects, TestimonialSection, Testimonial

# Register your models here.

admin.site.register(Banner)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')

    def has_add_permission(self, request):
        # Prevent adding more than one About Us instance
        if AboutUs.objects.exists():
            return False
        return True
    

admin.site.register(AboutUs, AboutUsAdmin)


class AboutServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name',)

    def has_add_permission(self, request):
        # Prevent adding more than 4 About Services instances
        if AboutServices.objects.count() >= 4:
            return False
        return True

admin.site.register(AboutServices, AboutServicesAdmin)


class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')

    def has_add_permission(self, request):
        # Prevent adding more than one Why Us instance
        if WhyUs.objects.exists():
            return False
        return True
    
admin.site.register(WhyUs, WhyUsAdmin)



class MainServicesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')

    def has_add_permission(self, request):
        # Prevent adding more than one Main Services instance
        if MainServices.objects.exists():
            return False
        return True
    
admin.site.register(MainServices, MainServicesAdmin)


class SpecializedInAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')

    def has_add_permission(self, request):
        # Prevent adding more than one Specialized In instance
        if SpecializedIn.objects.exists():
            return False
        return True
    
admin.site.register(SpecializedIn, SpecializedInAdmin)



class SpecializedInServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title',)

    def has_add_permission(self, request):
        # Prevent adding more than 4 Specialized In Services instances
        if SpecializedInServices.objects.count() >= 6:
            return False

        return True


class ProjectSectionTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        # Prevent adding more than one Project Section Title In instance
        if ProjectSectionTitle.objects.exists():
            return False
        return True

admin.site.register(ProjectSectionTitle, ProjectSectionTitleAdmin)


admin.site.register(Projects)


class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ('heading', 'sub_heading')

    def has_add_permission(self, request):
        # Prevent adding more than one Testimonial Section instance
        if TestimonialSection.objects.exists():
            return False
        return True
    
admin.site.register(TestimonialSection, TestimonialSectionAdmin)
    

    
admin.site.register(Testimonial)
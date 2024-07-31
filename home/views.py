from django.shortcuts import render
from contact_us.models import ContactInfo
from home.models import Banner, AboutUs, AboutServices, WhyUs, MainServices, SpecializedIn, SpecializedInServices, ProjectSectionTitle, Projects, TestimonialSection, Testimonial

# Create your views here.


def home(request):
    data = {
        "contact_data": ContactInfo.objects.first(),
        "banners": Banner.objects.all(),
        "about_us": AboutUs.objects.first(),
        "about_services": AboutServices.objects.all(),
        "why_us": WhyUs.objects.first(),
        "specialized_in": SpecializedIn.objects.first(),
        'specialized_in_services': SpecializedInServices.objects.all(),
        "main_services": MainServices.objects.first(),
        "project_section_title": ProjectSectionTitle.objects.first(),
        "projects": Projects.objects.all(),
        "testimonial_section": TestimonialSection.objects.first(),
        "testimonials": Testimonial.objects.all(),
    }
    
    return render(request, template_name="home/home.html", context=data)

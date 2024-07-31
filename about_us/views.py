from django.shortcuts import render
from about_us.models import Banner, CompanyProfile
from contact_us.models import ContactInfo
from home.models import WhyUs, TestimonialSection, Testimonial



# Create your views here.

def about_us(request):
    data = {
        "banner": Banner.objects.first(),
        "company_profile": CompanyProfile.objects.first(),
        "why_us": WhyUs.objects.first(),
        "testimonial_section": TestimonialSection.objects.first(),
        "testimonials": Testimonial.objects.all(),
        "contact_data": ContactInfo.objects.first(),
    }
    return render(request, template_name="about_us/about-us.html", context=data)

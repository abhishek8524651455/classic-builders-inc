from django.shortcuts import render
from contact_us.models import Banner, ContactInfo


# Create your views here.

def contact_us(request):
    contact_data = {
        "banner": Banner.objects.first(),
        "contact_data": ContactInfo.objects.first()
    }
    return render(request, 'contact_us/contact-us.html', context=contact_data)


from django.shortcuts import render
from contact_us.models import ContactInfo
from services.models import Banner, PostBannerContent, Services

# Create your views here.

def service_page(request):
    data = {
        "banner": Banner.objects.first(),
        "post_banner_content": PostBannerContent.objects.first(),
        "services": Services.objects.all(),
        "contact_data": ContactInfo.objects.first(),
    }

    return render(request, 'services/service-page.html', context=data)


def service_details(request, service_id):
    service = Services.objects.get(service_id=service_id)
    data = {
        "service": service,
    }
    return render(request, 'services/service-details.html', context=data)




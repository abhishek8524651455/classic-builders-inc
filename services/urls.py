from django.urls import path
from .views import service_page, service_details


app_name = "services"

urlpatterns = [
    path('', service_page, name='services'),
    path('<slug:service_id>/', service_details, name='service_details'),


    # path('<slug:service_page_slug>/', more_about_service, name='more_about_service')
]

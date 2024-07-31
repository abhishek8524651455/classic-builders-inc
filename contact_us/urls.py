from django.urls import path
from .views import contact_us


app_name = "contact_us"

urlpatterns = [
    path('', contact_us, name='contact-us')
]

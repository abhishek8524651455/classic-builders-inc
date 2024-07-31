from django.urls import path
from .views import news, detailed_news


app_name = "news"

urlpatterns = [
    path('', news, name='news'),
    path('<slug:news_id>/', detailed_news, name='detailed_news')
]

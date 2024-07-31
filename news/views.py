from django.shortcuts import render
from news.models import Banner, News
from contact_us.models import ContactInfo


# Create your views here.

def news(request):
    data = {
        "banner": Banner.objects.first(),
        "all_news": News.objects.all(),
        "contact_data": ContactInfo.objects.first(),
    }

    return render(request, 'news/news.html', context=data)


def detailed_news(request, news_id):
    data = {
        "news": News.objects.get(news_id=news_id),
        "contact_data": ContactInfo.objects.first(),
    }

    return render(request, 'news/detailed-news.html', context=data)

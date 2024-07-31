from django.urls import path
from .views import (
    login_view, home_view, banner_home,  about_as_home, why_us, main_services, specialized_in, projects, testimonials, 
    about_view, banner_about, company_profile, 
    services_overview, services_banner, post_banner_content, detailed_service, 
    news_overview, news_banner, post_news_banner_content, detailed_news, contact_overview,
    contact_overview, contact_banner, contact_info
    )

from django.contrib.auth.decorators import login_required

app_name = "builders_admin"

urlpatterns = [
    path('', login_view, name='login_view'),
    path('home/', login_required(home_view), name='home_view'),
    path('home/banner/', login_required(banner_home), name='banner_home'),
    path('home/about-us/', login_required(about_as_home), name='about_as_home'),
    path('home/why_us/', login_required(why_us), name='why_us'),
    path('home/main-services/', login_required(main_services), name='main_services'),
    path('home/specialized-in/', login_required(specialized_in), name='specialized_in'),
    path('home/recent-projects/', login_required(projects), name='recent_projects'),
    path('home/testimonials/', login_required(testimonials), name='testimonials'),


    path('about-us/', login_required(about_view), name='about_view'),
    path('about-us/banner', login_required(banner_about), name='banner_about'),
    path('about-us/company-profile', login_required(company_profile), name='company_profile'),

    path('services/', login_required(services_overview), name='services_overview'),
    path('services/banner/', login_required(services_banner), name='services_banner'),
    path('services/post-banner-content/', login_required(post_banner_content), name='post_banner_content'),
    path('services/post-banner-content/<slug:service_id>', login_required(detailed_service), name='detailed_service'),

    path('news/', login_required(news_overview), name='news_overview'),
    path('news/banner/', login_required(news_banner), name='news_banner'),
    path('news/post-banner', login_required(post_news_banner_content), name='post_news_banner_content'),
    path('news/post-banner/<slug:news_id>', login_required(detailed_news), name='detailed_news'),

    path('contact-us/', login_required(contact_overview), name='contact_overview'),
    path('contact-us/banner/', login_required(contact_banner), name='contact_banner'),
    path('contact-us/info/', login_required(contact_info), name='contact_info'),
]


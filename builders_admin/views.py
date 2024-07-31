from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from home.models import Banner, AboutUs, AboutServices, WhyUs, MainServices, SpecializedIn, SpecializedInServices, ProjectSectionTitle, Projects, TestimonialSection, Testimonial
from about_us.models import Banner as about_us_banner, CompanyProfile
from services.models import Banner as serv_banner, PostBannerContent, Services
from news.models import Banner as nw_banner, News
from contact_us.models import Banner as ct_banner, ContactInfo
import uuid
from django.contrib.auth.decorators import login_required



# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('builders_admin:home_view')
        else:
            return render(request, 'builders_admin/login.html', {'error_message': True})

    return render(request, 'builders_admin/login.html')


def home_view(request):
    data = {
        "banners": Banner.objects.all(),
        "about_us": AboutUs.objects.first(),
        "about_services": AboutServices.objects.all(),
        'why_us': WhyUs.objects.first(),
        'main_services': MainServices.objects.first(),
        "specialized_in": SpecializedIn.objects.first(),
        'specialized_in_services': SpecializedInServices.objects.all(),
        "project_section_title": ProjectSectionTitle.objects.first(),
        'projects': Projects.objects.all(),
        "testimonial_section": TestimonialSection.objects.first(),
        "testimonials": Testimonial.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'home'
    }
    return render(request, 'builders_admin/home/home.html', context=data)


def banner_home(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        banner_id = request.POST.get("object-id")
        heading = request.POST.get("heading")
        sub_heading = request.POST.get("sub-heading")
        description = request.POST.get("banner-description")
        button_text = request.POST.get("read-more")
        image = request.FILES.get("image")

        if action == 'update':
            try:
                banner = Banner.objects.get(id=banner_id)
                banner.heading = heading
                banner.sub_heading = sub_heading
                banner.description = description
                banner.button_text = button_text
                if image:
                    banner.image = image

                banner.save()

            except Exception as e:
                print(e)

        elif action == 'delete':
            total_banners = Banner.objects.count()
            
            if total_banners >= 2:
                try:
                    banner = Banner.objects.get(id=banner_id)
                    banner.delete()

                except Exception as e:
                    print(e)

            else:
                pass

        elif action == 'add':
            last_banner = Banner.objects.order_by('-id').first()
            
            new_banner = Banner(
                image=last_banner.image,
                heading=last_banner.heading,
                sub_heading=last_banner.sub_heading,
                description=last_banner.description,
                button_text=last_banner.button_text
            )
            new_banner.save()

    data = {
        "banners": Banner.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'banner'
    }

    return render(request, 'builders_admin/home/banner.html', context=data)


def about_as_home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'save-about-us':
            try:
                about_us_instance = AboutUs.objects.first()

                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub-heading")
                description = request.POST.get("banner-description")

                about_us_instance.heading = heading
                about_us_instance.sub_heading = sub_heading
                about_us_instance.description = description
                about_us_instance.save()
            
            except Exception as e:
                print(e)

        elif action == 'update':
            try:
                object_id = request.POST.get('object-id')
                service_name = request.POST.get('service-name')
                service_image = request.FILES.get("service-image")
                service_icon = request.FILES.get("service-icon")

                about_us_service = AboutServices.objects.get(id=object_id)

                about_us_service.service_name = service_name
                if service_image:
                    about_us_service.service_image = service_image
                
                if service_icon:
                    about_us_service.service_icon = service_icon
                
                about_us_service.save()

            except Exception as e:
                print(e)

        elif action == 'add':
            try:
                last_service = AboutServices.objects.order_by('-id').first()

                new_service = AboutServices(
                    service_name=last_service.service_name,
                    service_image=last_service.service_image,
                    service_icon=last_service.service_icon,
                )

                new_service.save()
            
            except Exception as e:
                print(e)

        elif action == 'delete':
            object_id = request.POST.get('object-id')
            total_services = AboutServices.objects.count()
            
            if total_services >= 2:
                try:
                    service = AboutServices.objects.get(id=object_id)
                    service.delete()

                except Exception as e:
                    print(e)

            else:
                pass

        
    data = {
        'about_us_instance': AboutUs.objects.first(),
        'about_us_services': AboutServices.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'about-us'
    }
    return render(request, 'builders_admin/home/about-us.html', context=data)



def why_us(request):
    if request.method == 'POST':

        action = request.POST.get('action')
        
        if action == 'update':

            try:
                why_us_instance = WhyUs.objects.first()

                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub-heading")
                description = request.POST.get("description")
                image = request.FILES.get("image")
                image_text = request.POST.get("image-text")
                mission_heading = request.POST.get("mission-heading")
                mission_text = request.POST.get("mission-text")
                vision_heading = request.POST.get("vision-heading")
                vision_text = request.POST.get("vision-text")

                why_us_instance.heading = heading
                why_us_instance.sub_heading = sub_heading
                why_us_instance.description = description
                why_us_instance.image_text = image_text
                why_us_instance.mission_heading = mission_heading
                why_us_instance.mission_text = mission_text
                why_us_instance.vision_heading = vision_heading
                why_us_instance.vision_text = vision_text
            
                if image:
                    why_us_instance.image = image


                why_us_instance.save()

            except Exception as e:
                print(e)


    data = {
        "why_us": WhyUs.objects.first(),
        'current_view': 'home',
        'current_sub_view': 'why-us'

    }

    return render(request, 'builders_admin/home/why-us.html', context=data)


def main_services(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'update':
            try:
                main_services_instance = MainServices.objects.first()

                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub-heading")
                description = request.POST.get("description")
                service_1_title = request.POST.get("service_1_title")
                service_1_image = request.FILES.get("service-image-1")
                service_2_title = request.POST.get("service_2_title")
                service_2_image = request.FILES.get("service-image-2")
                service_3_title = request.POST.get("service_3_title")
                service_3_image = request.FILES.get("service-image-3")
                button_text = request.POST.get("button_text")

                main_services_instance.heading = heading
                main_services_instance.sub_heading = sub_heading
                main_services_instance.description = description
                main_services_instance.service_1_title = service_1_title
                main_services_instance.service_2_title = service_2_title
                main_services_instance.service_3_title = service_3_title
                main_services_instance.button_text = button_text

                if service_1_image:
                    main_services_instance.service_1_image = service_1_image
                if service_2_image:
                    main_services_instance.service_2_image = service_2_image
                if service_3_image:
                    main_services_instance.service_3_image = service_3_image

                main_services_instance.save()


            except Exception as e:
                print(e)

    data = {
        'main_services': MainServices.objects.first(),
        'current_view': 'home',
        'current_sub_view': 'main_services'
    }

    return render(request, 'builders_admin/home/main-services.html', context=data)


def specialized_in(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'save_specialized':
            try:
                specialized_in_instance = SpecializedIn.objects.first()

            except Exception as e:
                print(e)

        elif action == 'add_services':
            try:
                last_service = SpecializedInServices.objects.order_by('-id').first()
                new_service = SpecializedInServices(service_title=last_service.service_title)
                new_service.save()

            except Exception as e:
                print(e)


        elif action == 'remove_services':
            try:
                service_id = request.POST.get("object-id")
                service = SpecializedInServices.objects.get(id=service_id)
                service.delete()

            except Exception as e:
                print(e)

        elif action == 'update_services':
            try:
                service_id = request.POST.get("object-id")
                print(service_id)

                service_title = request.POST.get("service-title")
                print(service_title)
                service = SpecializedInServices.objects.get(id=service_id)
                service.service_title = service_title
                service.save()

            except Exception as e:
                print(e)

        elif action == 'update_specialized_top':
            try:
                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub-heading")
                description = request.POST.get("description")

                specialized_in_instance = SpecializedIn.objects.first()
                specialized_in_instance.heading = heading
                specialized_in_instance.sub_heading = sub_heading
                specialized_in_instance.description = description
                specialized_in_instance.save()

            except Exception as e:
                print(e)

        elif action == 'update_specialized_image':
            try:
                specialized_in_instance = SpecializedIn.objects.first()
                image = request.FILES.get("image")

                if image:
                    specialized_in_instance.image = image
                    specialized_in_instance.save()

            except Exception as e:
                print(e)

        elif action == 'update_specialized_subsection':
            try:
                specialized_in_instance = SpecializedIn.objects.first()

                heading_2 = request.POST.get("heading-2")
                sub_heading_2 = request.POST.get("sub-heading-2")
                subsection_heading = request.POST.get("subsection-heading")

                specialized_in_instance.heading_2 = heading_2
                specialized_in_instance.sub_heading_2 = sub_heading_2
                specialized_in_instance.subsection_heading = subsection_heading
                specialized_in_instance.save()
            
            except Exception as e:
                print(e)

    data = {
        'specialized_in': SpecializedIn.objects.first(),
        'specialized_in_services': SpecializedInServices.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'specialized_in'
    }

    return render(request, 'builders_admin/home/specialized-in.html', context=data)



def projects(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_title':
            try:
                title = request.POST.get("project_section_title")
                sectionTitle = ProjectSectionTitle.objects.first()
                sectionTitle.title = title
                sectionTitle.save()

            except Exception as e:
                print(e)
            
        elif action == 'add':
            try:
                last_project = Projects.objects.order_by('-id').first()
                new_project = Projects(name=last_project.name, image=last_project.image)
                new_project.save()

            except Exception as e:
                print(e)

        elif action == 'remove':
            try:
                project_id = request.POST.get("object-id")
                project = Projects.objects.get(id=project_id)
                project.delete()

            except Exception as e:
                print(e)

        elif action == 'update':
            try:
                project_id = request.POST.get("object-id")
                project_name = request.POST.get("project-name")
                project_image = request.FILES.get("project-image")

                project = Projects.objects.get(id=project_id)
                project.name = project_name

                if project_image:
                    project.image = project_image

                project.save()

            except Exception as e:
                print(e)


    data = {
        "project_section_title": ProjectSectionTitle.objects.first(),
        'projects': Projects.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'projects'
    }

    return render(request, 'builders_admin/home/recent-projects.html', context=data)



def testimonials(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update_testimonial_section':
            try:
                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub_heading")
                description = request.POST.get("description")

                testimonial_section = TestimonialSection.objects.first()

                testimonial_section.heading = heading
                testimonial_section.sub_heading = sub_heading
                testimonial_section.description = description
                testimonial_section.save()
                

            except Exception as e:
                print(e)

        elif action == 'update_testimonial':

            try:
                testimonial_id = request.POST.get("object-id")
                author = request.POST.get("author")
                review = request.POST.get("review")
                image = request.FILES.get("image")

                testimonial = Testimonial.objects.get(id=testimonial_id)
                testimonial.author = author
                testimonial.review = review
                
                if image:
                    testimonial.image = image

                testimonial.save()

            except Exception as e:
                print(e)


        elif action == 'remove_testimonial':
            try:
                testimonial_id = request.POST.get("object-id")
                testimonial = Testimonial.objects.get(id=testimonial_id)
                testimonial.delete()
            
            except Exception as e:
                print(e)

        elif action == 'add_testimonial':
            try:
                last_testimonial = Testimonial.objects.order_by('-id').first()
                new_testimonial = Testimonial(author=last_testimonial.author, review=last_testimonial.review, image=last_testimonial.image)
                new_testimonial.save()

            except Exception as e:
                print(e)
    


    data = {
        "testimonial_section": TestimonialSection.objects.first(),
        "testimonials": Testimonial.objects.all(),
        'current_view': 'home',
        'current_sub_view': 'testimonial'
    }

    return render(request, 'builders_admin/home/testimonials.html', context=data)




def about_view(request):
    data = {
        "banner": about_us_banner.objects.first(),
        'current_view': 'about-us',
        'current_sub_view': 'about-us-2'
    }

    return render(request, 'builders_admin/about-us/about-us.html', context=data)

def banner_about(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update':
            try:
                heading = request.POST.get("heading")
                image = request.FILES.get("image")

                banner = about_us_banner.objects.first()

                banner.heading = heading

                if image:
                    banner.image = image

                banner.save()

            except Exception as e:
                print(e)


    data = {
        "banner": about_us_banner.objects.first(),
        'current_view': 'about-us',
        'current_sub_view': 'banner-about'
    }
    return render(request, 'builders_admin/about-us/banner.html', context=data)


def company_profile(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            try:
                image = request.FILES.get("image")
                heading = request.POST.get("heading")
                sub_heading = request.POST.get("sub_heading")
                description = request.POST.get("description")

                company_profile = CompanyProfile.objects.first()
                company_profile.heading = heading
                company_profile.sub_heading = sub_heading
                company_profile.description = description

                if image:
                    company_profile.image = image
                    
                company_profile.save()

            except Exception as e:
                print(e)

    data = {
        "company_profile": CompanyProfile.objects.first(),
        'current_view': 'about-us',
        'current_sub_view': 'company-profile'
    }
    return render(request, 'builders_admin/about-us/company-profile.html', context=data)



def services_overview(request):
    data = {
        "banner": serv_banner.objects.first(),
        "post_banner_content": PostBannerContent.objects.first(),
        "services": Services.objects.all(),
        'current_view': 'services-overview',
        'current_sub_view': 'services-overview'
    }

    return render(request, 'builders_admin/services/services.html', context=data)


def services_banner(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            try:
                heading = request.POST.get("heading")
                image = request.FILES.get("image")

                banner = serv_banner.objects.first()
                banner.heading = heading

                if image:
                    banner.image = image

                banner.save()

            except Exception as e:
                print(e)
    data = {
        
        "banner": serv_banner.objects.first(),
        'current_view': 'services-overview',
        'current_sub_view': 'services_banner'
    }

    return render(request, 'builders_admin/services/banner.html', context=data)


def post_banner_content(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update-post-banner-content':
            try:
                heading = request.POST.get("heading")
                description = request.POST.get("description")

                banner = PostBannerContent.objects.first()
                banner.heading = heading
                banner.description = description

                banner.save()

            except Exception as e:
                print(e)

        elif action == 'update-post-banner-services':
            try:
                object_id = request.POST.get("object-id")
                thumbnail = request.FILES.get("thumbnail")
                short_heading = request.POST.get("short-heading")
                short_description = request.POST.get("short-description")
                info_button_text = request.POST.get("info-button-text")

                service = Services.objects.get(service_id=object_id)

                service.short_heading = short_heading
                service.short_description = short_description
                service.info_button_text = info_button_text

                if thumbnail:
                    service.thumbnail = thumbnail

                service.save()

            except Exception as e:
                print(e)

        elif action == 'add-more-services':
            try:
                last_service = Services.objects.latest('service_id')

                new_service = Services(
                    service_id=str(uuid.uuid4()),
                    thumbnail=last_service.thumbnail,
                    short_heading=last_service.short_heading,
                    short_description=last_service.short_description,
                    info_button_text=last_service.info_button_text,
                    heading=last_service.heading,
                    description=last_service.description,
                    book_now_button_text=last_service.book_now_button_text,
                    image=last_service.image,
                    before_after_heading=last_service.before_after_heading,
                    before_image=last_service.before_image,
                    after_image=last_service.after_image
                    )

                new_service.save()

            except Exception as e:
                print(e)


        elif action == 'remove-service':
            try:
                service_id = request.POST.get("object-id")
                service = Services.objects.get(service_id=service_id)
                service.delete()

            except Exception as e:
                print(e)

    data = {
        "services": Services.objects.all(),
        "content": PostBannerContent.objects.first(),
        'current_view': 'services-overview',
        'current_sub_view': 'post_banner_content'
    }

    return render(request, 'builders_admin/services/post-banner.html', context=data)

def detailed_service(request, service_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update-service-details':
            try:
                description = request.POST.get("description")
                book_now_button_text = request.POST.get("book_now_button_text")
                image = request.FILES.get("image")

                service = Services.objects.get(service_id=service_id)

                service.description = description
                service.book_now_button_text = book_now_button_text

                if image:
                    service.image = image

                service.save()

            except Exception as e:
                print(e)


        elif action == 'update-before-after':
            try:
                before_after_heading = request.POST.get("before_after_heading")

                before_image = request.FILES.get("before_image")
                after_image = request.FILES.get("after_image")

                service = Services.objects.get(service_id=service_id)

                service.before_after_heading = before_after_heading

                if before_image:
                    service.before_image = before_image

                if after_image:
                    service.after_image = after_image

                service.save()

            except Exception as e:
                print(e)

    data = {
        "service": Services.objects.get(service_id=service_id),
    }

    return render(request, 'builders_admin/services/service-details.html', context=data)


def news_overview(request):
    data = {
        "banner": nw_banner.objects.first(),
        "all_news": News.objects.all(),
        'current_view': 'news-overview',
        'current_sub_view': 'news-overview',
    }

    return render(request, 'builders_admin/news/news.html', context=data)


def news_banner(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            try:
                heading = request.POST.get("heading")
                image = request.FILES.get("image")

                banner = nw_banner.objects.first()
                banner.heading = heading

                if image:
                    banner.image = image

                banner.save()

            except Exception as e:
                print(e)
    data = {
        "banner": nw_banner.objects.first(),
        'current_view': 'news-overview',
        'current_sub_view': 'news_banner'
    }

    return render(request, 'builders_admin/news/banner.html', context=data)


def post_news_banner_content(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update-news-card':
            try:
                object_id = request.POST.get("object-id")
                thumbnail = request.FILES.get("thumbnail")
                short_heading = request.POST.get("short_heading")
                short_description = request.POST.get("short_description")
                info_button_text = request.POST.get("info_button_text")

                news_card = News.objects.get(news_id=object_id)
                news_card.short_heading = short_heading
                news_card.short_description = short_description
                news_card.info_button_text = info_button_text
                
                if thumbnail:
                    news_card.thumbnail = thumbnail

                news_card.save()

            except Exception as e:
                print(e)

        elif action == 'add-more-news':
            try:
                last_news = News.objects.latest('news_id')
                new_news = News(
                    news_id=str(uuid.uuid4()),
                    thumbnail=last_news.thumbnail,
                    short_heading=last_news.short_heading, 
                    short_description=last_news.short_description, 
                    info_button_text=last_news.info_button_text,
                    image=last_news.image,
                    heading=last_news.heading,
                    description=last_news.description,
                    )
                    
                new_news.save()

            except Exception as e:
                print(e)

        elif action == 'remove-news-card':
            try:
                news_id = request.POST.get("object-id")
                news = News.objects.get(news_id=news_id)
                news.delete()

            except Exception as e:
                print(e)


    data = {
        'all_news': News.objects.all(),
        'current_view': 'news-overview',
        'current_sub_view': 'post_news_banner_content'
    }

    return render(request, 'builders_admin/news/post-banner.html', context=data)


def detailed_news(request, news_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update-news-details':
            try:
                heading = request.POST.get("heading")
                description = request.POST.get("description")
                image = request.FILES.get("image")

                news = News.objects.get(news_id=news_id)

                news.heading = heading
                news.description = description
                
                if image:
                    news.image = image

                news.save()

            except Exception as e:
                print(e)


    data = {
        'news': News.objects.get(news_id=news_id),
        'current_view': 'news-overview',
        'current_sub_view': 'detailed_news'
    }

    return render(request, 'builders_admin/news/news-details.html', context=data)


def contact_overview(request):
    data = {
        "banner": ct_banner.objects.first(),
        "contact_info": ContactInfo.objects.first(),
        'current_view': 'contact-overview',
        'current_sub_view': 'contact-overview',
    }

    return render(request, 'builders_admin/contact-us/contact-us.html', context=data)


def contact_banner(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            try:
                heading = request.POST.get("heading")
                image = request.FILES.get("image")

                banner = ct_banner.objects.first()
                banner.heading = heading

                if image:
                    banner.image = image

                banner.save()

            except Exception as e:
                print(e)

    data = {
        "banner": ct_banner.objects.first(),
        'current_view': 'contact-overview',
        'current_sub_view': 'contact_banner'
    }

    return render(request, 'builders_admin/contact-us/banner.html', context=data)

def contact_info(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update':
            try:
                company_name = request.POST.get("company_name")
                phone_number = request.POST.get("phone_number")
                email = request.POST.get("email")
                address = request.POST.get("address")
                facebook_link = request.POST.get("facebook_link")
                twitter_link = request.POST.get("twitter_link")
                linkedin_link = request.POST.get("linkedin_link")
                contact_page_image = request.FILES.get("contact_page_image")

                contact_info = ContactInfo.objects.first()
                contact_info.company_name = company_name
                contact_info.phone_number = phone_number
                contact_info.email = email
                contact_info.address = address
                contact_info.facebook_link = facebook_link
                contact_info.twitter_link = twitter_link
                contact_info.linkedin_link = linkedin_link

                if contact_page_image:
                    contact_info.contact_page_image = contact_page_image

                contact_info.save()

            except Exception as e:
                print(e)
    data = {
        "contact_info": ContactInfo.objects.first(),
        'current_view': 'contact-overview',
        'current_sub_view': 'contact_info'
    }

    return render(request, 'builders_admin/contact-us/contact-info.html', context=data)
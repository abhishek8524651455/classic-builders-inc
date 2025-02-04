# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AboutUsBanner(models.Model):
    heading = models.CharField(max_length=150)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'about_us_banner'


class AboutUsCompanyprofile(models.Model):
    image = models.CharField(max_length=100)
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'about_us_companyprofile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BuildersAdminCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'builders_admin_customuser'


class BuildersAdminCustomuserGroups(models.Model):
    customuser = models.ForeignKey(BuildersAdminCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'builders_admin_customuser_groups'
        unique_together = (('customuser', 'group'),)


class BuildersAdminCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(BuildersAdminCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'builders_admin_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class ContactUsContactinfo(models.Model):
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    facebook_link = models.TextField()
    twitter_link = models.TextField()
    linkedin_link = models.TextField()
    contact_page_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'contact_us_contactinfo'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(BuildersAdminCustomuser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HomeAboutservices(models.Model):
    service_icon = models.CharField(max_length=100)
    service_image = models.CharField(max_length=100)
    service_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_aboutservices'


class HomeAboutus(models.Model):
    heading = models.CharField(max_length=40)
    sub_heading = models.CharField(max_length=40)
    description = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'home_aboutus'


class HomeBanner(models.Model):
    image = models.CharField(max_length=100)
    heading = models.CharField(max_length=40)
    button_text = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    sub_heading = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'home_banner'


class HomeMainservices(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    service_1_title = models.CharField(max_length=100)
    service_1_image = models.CharField(max_length=100)
    service_2_title = models.CharField(max_length=100)
    service_2_image = models.CharField(max_length=100)
    service_3_title = models.CharField(max_length=100)
    service_3_image = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'home_mainservices'


class HomeProjects(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'home_projects'


class HomeProjectsectiontitle(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'home_projectsectiontitle'


class HomeSpecializedin(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    image = models.CharField(max_length=100)
    subsection_heading = models.CharField(max_length=300)
    heading_2 = models.CharField(max_length=150)
    sub_heading_2 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'home_specializedin'


class HomeSpecializedinservices(models.Model):
    service_title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'home_specializedinservices'


class HomeTestimonial(models.Model):
    author = models.CharField(max_length=150)
    review = models.CharField(max_length=2000)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'home_testimonial'


class HomeTestimonialsection(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'home_testimonialsection'


class HomeWhyus(models.Model):
    heading = models.CharField(max_length=150)
    sub_heading = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    image_text = models.CharField(max_length=100)
    mission_heading = models.CharField(max_length=40)
    mission_text = models.CharField(max_length=250)
    vision_heading = models.CharField(max_length=40)
    vision_text = models.CharField(max_length=250)
    description = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'home_whyus'


class NewsBanner(models.Model):
    image = models.CharField(max_length=100)
    heading = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'news_banner'


class NewsNews(models.Model):
    thumbnail = models.CharField(max_length=100)
    short_heading = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300)
    info_button_text = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = 'news_news'


class ServicesBanner(models.Model):
    image = models.CharField(max_length=100)
    heading = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'services_banner'


class ServicesPostbannercontent(models.Model):
    heading = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'services_postbannercontent'


class ServicesServices(models.Model):
    short_heading = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300)
    info_button_text = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    description = models.TextField()
    book_now_button_text = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    before_after_heading = models.CharField(max_length=300)
    before_image = models.CharField(max_length=100)
    after_image = models.CharField(max_length=100)
    service_id = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'services_services'

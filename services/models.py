from django.db import models
import uuid
import os
import re


# Create your models here.


class Banner(models.Model):
    image = models.ImageField(upload_to='static/uploads/services/banners', blank=True)
    heading = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and Banner.objects.exists():
            raise ValidationError('There can be only one Banner instance')
        
        return super(Banner, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'


    def __str__(self):
        return self.heading

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())


class PostBannerContent(models.Model):
    heading = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and PostBannerContent.objects.exists():
            raise ValidationError('There can be only one Post Banner Content instance')
        
        return super(PostBannerContent, self).save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Post Banner Content'
        verbose_name_plural = 'Post Banner Content'


class Services(models.Model):
    service_id = models.UUIDField(primary_key=True, default=str(uuid.uuid4), editable=False)
    thumbnail = models.ImageField(upload_to='static/uploads/services/thumbnails', blank=True)
    short_heading = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    info_button_text = models.CharField(max_length=100, blank=True)
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    book_now_button_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='static/uploads/services', blank=True)
    before_after_heading = models.CharField(max_length=300, blank=True)
    before_image = models.ImageField(upload_to='static/uploads/services/before-after/before', blank=True)
    after_image = models.ImageField(upload_to='static/uploads/services/before-after/after', blank=True)


    @property
    def alt_thumbnail(self):
        filename = os.path.basename(self.thumbnail.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    @property
    def alt_before_image(self):
        filename = os.path.basename(self.before_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    @property
    def alt_after_image(self):
        filename = os.path.basename(self.after_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())
    
    @property
    def slug_id(self):
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(self.heading)[0]).replace(" ", "-").lower())
    


    def __str__(self):
        return self.short_heading
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
    













# class ServicePage(models.Model):
#     meta_title = models.CharField(max_length=200)
#     meta_keywords = models.CharField(max_length=200)
#     meta_description = models.CharField(max_length=200)
    
#     def save(self, *args, **kwargs):
#         if not self.pk and ServicePage.objects.exists():
#             raise ValidationError('There can be only one Service Page instance')
#         return super(ServicePage, self).save(*args, **kwargs)

#     class Meta:
#         verbose_name = 'Service Page'  # Singular name for the model
#         verbose_name_plural = 'Service Page'  # Plural name for the model

#     def __str__(self):
#         return self.meta_title
    

# class DetailedService(models.Model):
#     meta_title = models.CharField(max_length=200)
#     meta_keywords = models.CharField(max_length=200)
#     meta_description = models.CharField(max_length=200)
#     short_title = models.CharField(max_length=50)
#     short_description = models.CharField(max_length=500)
#     know_more_button = models.CharField(max_length=100)
#     thumbnail = models.ImageField(upload_to='static/images')
#     service_page_slug = models.SlugField(max_length=100, primary_key=True, editable=False)
#     title = models.CharField(max_length=400)
#     display_image = models.ImageField(upload_to='static/images')
#     content = HTMLField()
#     book_now_button_text = models.CharField(max_length=100)
#     call_now_button_text = models.CharField(max_length=100)
#     before_after_title = models.CharField(max_length=400)
#     before = models.ImageField(upload_to='static/images')
#     after = models.ImageField(upload_to='static/images')

#     def image_tag(self):
#         return format_html(f"<img src='{self.thumbnail.url}' style='width: 40px; border-radius: 6px' />")

#     def __str__(self):
#         return self.short_title

#     class Meta:
#         verbose_name = 'Service Page'  # Singular name for the model
#         verbose_name_plural = 'Service Page'  # Plural name for the model
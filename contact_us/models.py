from django.db import models
import re
import uuid
import os

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='static/uploads/contact-us/banners', blank=True)
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

class ContactInfo(models.Model):
    company_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    facebook_link = models.TextField(blank=True)
    twitter_link = models.TextField(blank=True)
    linkedin_link = models.TextField(blank=True)
    contact_page_image = models.ImageField(upload_to='static/images')

    def save(self, *args, **kwargs):
        if not self.pk and ContactInfo.objects.exists():
            raise ValidationError('There can be only one ContactInfo instance')
        return super(ContactInfo, self).save(*args, **kwargs)
    
    @property
    def phone_number_link(self):
        return f"tel:{self.phone_number}"
    
    @property
    def email_link(self):
        return f"mailto:{self.email}"
    
    @property
    def contact_page_image_alt(self):
        if self.contact_page_image:
            file_name = os.path.basename(self.contact_page_image.name)
            return ((re.sub(r'[\W_]+', ' ', os.path.splitext(file_name)[0])).replace(" ", "-")).lower()
        
        else:
            file_name = "no image uploaded"
            return file_name

    

    class Meta:
        verbose_name = 'Contact Info'  # Singular name for the model
        verbose_name_plural = 'Contact Info'  # Plural name for the model
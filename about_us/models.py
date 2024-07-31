from django.db import models
import os
import re

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='static/uploads/about-us/banners', blank=True)
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


class CompanyProfile(models.Model):
    image = models.ImageField(upload_to='static/uploads/about-us', blank=True)
    heading = models.CharField(max_length=150, blank=True)
    sub_heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and CompanyProfile.objects.exists():
            raise ValidationError('There can be only one Company Profile instance')
        
        return super(CompanyProfile, self).save(*args, **kwargs)

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    def __str__(self):
        return self.heading


    class Meta:
        verbose_name = 'Company Profile'
        verbose_name_plural = 'Company Profile'
    



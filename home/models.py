from django.core.exceptions import ValidationError
from django.db import models
import re
import os

# Create your models here.


class Banner(models.Model):
    image = models.ImageField(upload_to='static/uploads/banners', blank=True)
    heading = models.CharField(max_length=40, blank=True)
    sub_heading = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=250, blank=True)
    button_text = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.heading

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())
    
    class Meta:
        verbose_name = 'Banner'  # Singular name for the model
        verbose_name_plural = 'Banner'  # Plural name for the model
    

class AboutUs(models.Model):
    heading = models.CharField(max_length=40, blank=True)
    sub_heading = models.CharField(max_length=40, blank=True)
    description = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            raise ValidationError('There can be only one About Us instance')
        
        return super(AboutUs, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class AboutServices(models.Model):
    service_icon = models.ImageField(upload_to='static/uploads/services/icons', blank=True)
    service_name = models.CharField(max_length=40, blank=True, null=True)
    service_image = models.ImageField(upload_to='static/uploads/services', blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and AboutServices.objects.count() >= 4:
            raise ValidationError('You can only create a maximum of 4 About US Services instances')
        
        return super(AboutServices, self).save(*args, **kwargs)
    
    @property
    def alt_service_icon(self):
        filename = os.path.basename(self.service_icon.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())
    
    @property
    def alt_service_image(self):
        filename = os.path.basename(self.service_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())
    

    
    class Meta:
        verbose_name = 'About Services'
        verbose_name_plural = 'About Services'
    


class WhyUs(models.Model):
    heading = models.CharField(max_length=150, blank=True)
    sub_heading = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='static/uploads/why-us', blank=True)
    image_text = models.CharField(max_length=100, blank=True)
    mission_heading = models.CharField(max_length=40, blank=True)
    mission_text = models.CharField(max_length=250, blank=True)
    vision_heading = models.CharField(max_length=40, blank=True)
    vision_text = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and WhyUs.objects.exists():
            raise ValidationError('There can be only one Why Us instance')
        
        return super(WhyUs, self).save(*args, **kwargs)
    
    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())
    

    class Meta:
        verbose_name = 'Why Us'
        verbose_name_plural = 'Why Us'


class MainServices(models.Model):
    heading = models.CharField(max_length=150, blank=True)
    sub_heading = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=300, blank=True)
    service_1_title = models.CharField(max_length=100, blank=True)
    service_1_image = models.ImageField(upload_to='static/uploads/main-services', blank=True)
    service_2_title = models.CharField(max_length=100, blank=True)
    service_2_image = models.ImageField(upload_to='static/uploads/main-services', blank=True)
    service_3_title = models.CharField(max_length=100, blank=True)
    service_3_image = models.ImageField(upload_to='static/uploads/main-services', blank=True)
    button_text = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and MainServices.objects.exists():
            raise ValidationError('There can be only one Main Services instance')
        
        return super(MainServices, self).save(*args, **kwargs)

    @property
    def alt_service_1_image(self):
        filename = os.path.basename(self.service_1_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    @property
    def alt_service_2_image(self):
        filename = os.path.basename(self.service_2_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    @property
    def alt_service_3_image(self):
        filename = os.path.basename(self.service_3_image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    class Meta:
        verbose_name = 'Main Services'
        verbose_name_plural = 'Main Services'



class SpecializedIn(models.Model):
    heading = models.CharField(max_length=150, blank=True)
    sub_heading = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='static/uploads/specialized-in', blank=True)
    heading_2 = models.CharField(max_length=150, blank=True)
    sub_heading_2 = models.CharField(max_length=200, blank=True)
    subsection_heading = models.CharField(max_length=300, blank=True)


    def save(self, *args, **kwargs):
        if not self.pk and SpecializedIn.objects.exists():
            raise ValidationError('There can be only one Specialized In instance')
        
        return super(SpecializedIn, self).save(*args, **kwargs)

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    class Meta:
        verbose_name = 'Specialized In'
        verbose_name_plural = 'Specialized In'


class SpecializedInServices(models.Model):
    service_title = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and SpecializedInServices.objects.count() >= 6:
            raise ValidationError('You can only create a maximum of 6 Specialized In Services instances')
        
        return super(SpecializedInServices, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Specialized In Services'
        verbose_name_plural = 'Specialized In Services'


class ProjectSectionTitle(models.Model):
    title = models.CharField(max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and ProjectSectionTitle.objects.exists():
            raise ValidationError('There can be only one Project Section Title In instance')
        
        return super(ProjectSectionTitle, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Project Section Title'
        verbose_name_plural = 'Project Section Title'

    def __str__(self):
        return self.title


class Projects(models.Model):
    name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='static/uploads/projects', blank=True)

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'


    def __str__(self):
        return self.name


class TestimonialSection(models.Model):
    heading = models.CharField(max_length=150, blank=True)
    sub_heading = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=300, blank=True)


    def save(self, *args, **kwargs):
        if not self.pk and TestimonialSection.objects.exists():
            raise ValidationError('There can be only one Testimonial Section instance')
        
        return super(TestimonialSection, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Testimonial Section'
        verbose_name_plural = 'Testimonial Section'


    def __str__(self):
        return self.heading


class Testimonial(models.Model):
    author = models.CharField(max_length=150, blank=True)
    review = models.CharField(max_length=2000, blank=True)
    image = models.ImageField(upload_to='static/uploads/testimonial', blank=True)

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return (re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower())

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonial'


    def __str__(self):
        return self.author
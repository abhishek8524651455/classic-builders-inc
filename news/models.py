from django.db import models
import os
import re
import uuid

# Create your models here.


class Banner(models.Model):
    image = models.ImageField(upload_to='static/uploads/news/banners', blank=True)
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
    

class News(models.Model):
    news_id = models.UUIDField(primary_key=True, default=str(uuid.uuid4), editable=False)
    thumbnail = models.ImageField(upload_to='static/uploads/news/thumbnails', blank=True)
    short_heading = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    info_button_text = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='static/uploads/news', blank=True)
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    @property
    def alt_thumbnail(self):
        filename = os.path.basename(self.thumbnail.name)
        return re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower()

    @property
    def alt_image(self):
        filename = os.path.basename(self.image.name)
        return re.sub(r'[\W_]+', ' ', os.path.splitext(filename)[0]).replace(" ", "-").lower()

    def __str__(self):
        return self.short_heading

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
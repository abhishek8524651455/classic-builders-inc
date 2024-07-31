# Generated by Django 5.0.6 on 2024-07-18 05:17

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_rename_services_servicepage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedService',
            fields=[
                ('meta_title', models.CharField(max_length=200)),
                ('meta_keywords', models.CharField(max_length=200)),
                ('meta_description', models.CharField(max_length=200)),
                ('short_title', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=500)),
                ('know_more_button', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='static/images')),
                ('service_page_slug', models.SlugField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('display_image', models.ImageField(upload_to='static/images')),
                ('content', tinymce.models.HTMLField()),
                ('book_now_button_text', models.CharField(max_length=100)),
                ('call_now_button_text', models.CharField(max_length=100)),
                ('before_after_title', models.CharField(max_length=400)),
                ('before', models.ImageField(upload_to='static/images')),
                ('after', models.ImageField(upload_to='static/images')),
            ],
            options={
                'verbose_name': 'Service Page',
                'verbose_name_plural': 'Service Page',
            },
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_alter_banner_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/uploads/about-us')),
                ('heading', models.CharField(blank=True, max_length=150)),
                ('sub_heading', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Company Profile',
                'verbose_name_plural': 'Company Profile',
            },
        ),
    ]

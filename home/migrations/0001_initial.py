# Generated by Django 5.0.6 on 2024-07-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/')),
                ('title', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('paragraph', models.CharField(max_length=500)),
                ('button_text', models.CharField(max_length=100)),
                ('button2_text', models.CharField(max_length=100)),
            ],
        ),
    ]

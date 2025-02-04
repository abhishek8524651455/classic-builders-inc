# Generated by Django 5.0.6 on 2024-07-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/uploads/banners')),
                ('heading', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
            },
        ),
    ]

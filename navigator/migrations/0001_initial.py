# Generated by Django 5.0.6 on 2024-07-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=10)),
                ('link_item_1', models.CharField(max_length=10)),
                ('title_2', models.CharField(blank=True, max_length=10)),
                ('link_item_2', models.CharField(blank=True, max_length=10)),
                ('title_3', models.CharField(blank=True, max_length=10)),
                ('link_item_3', models.CharField(blank=True, max_length=10)),
                ('title_4', models.CharField(blank=True, max_length=10)),
                ('link_item_4', models.CharField(blank=True, max_length=10)),
                ('title_5', models.CharField(blank=True, max_length=10)),
                ('link_item_5', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]

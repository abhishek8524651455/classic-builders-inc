# Generated by Django 5.0.6 on 2024-07-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='button_text',
            field=models.CharField(default='Read moe', max_length=40),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-07-25 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_aboutservices_alter_aboutus_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutservices',
            options={'verbose_name': 'About Services', 'verbose_name_plural': 'About Services'},
        ),
        migrations.RenameField(
            model_name='aboutservices',
            old_name='heading',
            new_name='service_name',
        ),
    ]

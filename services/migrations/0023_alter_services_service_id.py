# Generated by Django 5.0.3 on 2024-07-30 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_alter_services_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_id',
            field=models.UUIDField(default='<function uuid4 at 0x000002023DB4DBC0>', editable=False, primary_key=True, serialize=False),
        ),
    ]

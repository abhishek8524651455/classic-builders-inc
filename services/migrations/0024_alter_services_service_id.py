# Generated by Django 5.0.3 on 2024-07-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_alter_services_service_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_id',
            field=models.UUIDField(default='<function uuid4 at 0x00000205B298DBC0>', editable=False, primary_key=True, serialize=False),
        ),
    ]

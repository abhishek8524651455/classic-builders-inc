# Generated by Django 5.0.6 on 2024-07-31 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_news_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_id',
            field=models.UUIDField(default='<function uuid4 at 0x0000024E82EC3560>', editable=False, primary_key=True, serialize=False),
        ),
    ]

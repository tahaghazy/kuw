# Generated by Django 3.1.3 on 2020-11-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201115_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='post_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.3 on 2021-07-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_like_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_count',
        ),
    ]

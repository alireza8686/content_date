# Generated by Django 5.0.3 on 2024-03-26 19:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date_app', '0002_remove_day_height_remove_day_width_alter_day_month'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Day',
            new_name='DaysInformation',
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-09 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20190909_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscribe_expire',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# Generated by Django 2.2.4 on 2019-09-09 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_profile_subscribe_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscribe_expire',
            field=models.DateTimeField(),
        ),
    ]
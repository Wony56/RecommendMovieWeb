# Generated by Django 2.2.4 on 2019-09-09 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20190909_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subscribe_expire',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
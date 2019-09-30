# Generated by Django 2.2.4 on 2019-09-30 02:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=500)),
                ('view_cnt', models.IntegerField(default=0)),
                ('tmdb_id', models.IntegerField(default=0)),
                ('poster_path', models.TextField(default='')),
                ('overview', models.TextField(default='')),
                ('year', models.IntegerField(default=0)),
                ('rusercount', models.IntegerField(default=0)),
                ('rrating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('rgender', models.IntegerField(default=0)),
                ('academiceducatorcount', models.IntegerField(default=0)),
                ('artistcount', models.IntegerField(default=0)),
                ('clericaladmincount', models.IntegerField(default=0)),
                ('collegegradstudentcount', models.IntegerField(default=0)),
                ('customerservicecount', models.IntegerField(default=0)),
                ('doctorhealthcarecount', models.IntegerField(default=0)),
                ('executivemanagerialcount', models.IntegerField(default=0)),
                ('farmercount', models.IntegerField(default=0)),
                ('homemakercount', models.IntegerField(default=0)),
                ('K12studentcount', models.IntegerField(default=0)),
                ('lawyercount', models.IntegerField(default=0)),
                ('programmercount', models.IntegerField(default=0)),
                ('retiredcount', models.IntegerField(default=0)),
                ('salesmarketingcount', models.IntegerField(default=0)),
                ('scientistcount', models.IntegerField(default=0)),
                ('selfemployedcount', models.IntegerField(default=0)),
                ('technicianengineercount', models.IntegerField(default=0)),
                ('tradesmancraftsmancount', models.IntegerField(default=0)),
                ('unemployedcount', models.IntegerField(default=0)),
                ('writercount', models.IntegerField(default=0)),
                ('age1count', models.IntegerField(default=0)),
                ('age18count', models.IntegerField(default=0)),
                ('age25count', models.IntegerField(default=0)),
                ('age35count', models.IntegerField(default=0)),
                ('age45count', models.IntegerField(default=0)),
                ('age50count', models.IntegerField(default=0)),
                ('age56count', models.IntegerField(default=0)),
                ('othercount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timeStamp', models.DateTimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='M', max_length=10)),
                ('age', models.IntegerField(default=25)),
                ('occupation', models.CharField(max_length=200)),
                ('is_subscribe', models.BooleanField(default=False)),
                ('subscribe_expire', models.DateTimeField(default=datetime.datetime(2019, 9, 30, 11, 16, 43, 763815))),
                ('seenmovie', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='movieCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
            ],
        ),
    ]
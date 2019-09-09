# Generated by Django 2.2.4 on 2019-09-05 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usercluster'),
    ]

    operations = [
        migrations.CreateModel(
            name='movieCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
            ],
        ),
    ]

# Generated by Django 2.0 on 2018-04-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melon', '0004_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='profStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('button_status', models.BooleanField(default=True)),
                ('schedule_status', models.BooleanField(default=True)),
                ('sensor_status', models.BooleanField(default=True)),
            ],
        ),
    ]

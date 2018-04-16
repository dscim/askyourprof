# Generated by Django 2.0.4 on 2018-04-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.TextField(default='Event', verbose_name='Name of the event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(verbose_name='Day of the event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(verbose_name='Final time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(verbose_name='Starting time'),
        ),
    ]
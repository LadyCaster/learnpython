# Generated by Django 2.0.5 on 2018-06-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0016_auto_20180610_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moscowpythonmeetup',
            name='meetup_time',
            field=models.TimeField(blank=True, help_text='Время начала митапа', verbose_name='Время Митапа'),
        ),
    ]
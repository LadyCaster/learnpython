# Generated by Django 2.0.6 on 2018-06-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_auto_20180609_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courators',
            name='curator_photo',
            field=models.ImageField(blank=True, help_text='Фотография куратора', upload_to='courators/', verbose_name='Фото куратора'),
        ),
    ]
# Generated by Django 2.1.11 on 2019-12-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0033_auto_20191005_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learnpythoncourseprices',
            name='course_type',
            field=models.TextField(choices=[('Online', 'Online'), ('Offline', 'Offline'), ('OfflinePenza', 'OfflinePenza'), ('OfflineSpb', 'OfflineSpb')], help_text='Выберите тип курса', verbose_name='Тип курса'),
        ),
    ]

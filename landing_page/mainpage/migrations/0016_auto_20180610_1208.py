# Generated by Django 2.0.5 on 2018-06-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0015_auto_20180610_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduatestories',
            name='story_section',
            field=models.TextField(choices=[('Есть опыт, хочу освоить новый язык', 'Есть опыт, хочу освоить новый язык'), ('Никогда не программировал', 'Никогда не программировал'), ('Хочу новый навык или работу', 'Хочу новый навык или работу')], default='Никогда не программировал', help_text='В какую из секций историй', verbose_name='Раздел истории'),
        ),
    ]
# Generated by Django 4.2.4 on 2023-08-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0038_auto_20210803_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduatestories',
            name='story_section',
            field=models.TextField(choices=[('Есть опыт, хочу освоить новый язык', 'Есть опыт, хочу освоить новый язык'), ('Хочу новый навык или работу', 'Хочу новый навык или работу'), ('Никогда не программировал', 'Никогда не программировал')], default='Никогда не программировал', help_text='В какую из секций историй', verbose_name='Раздел истории'),
        ),
    ]

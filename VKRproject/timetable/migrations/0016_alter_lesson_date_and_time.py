# Generated by Django 4.1.7 on 2023-05-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0015_alter_lesson_date_and_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date_and_time',
            field=models.UUIDField(),
        ),
    ]
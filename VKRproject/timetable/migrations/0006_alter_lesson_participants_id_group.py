# Generated by Django 4.1.7 on 2023-05-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_alter_lesson_time_day_of_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_participants',
            name='id_group',
            field=models.UUIDField(),
        ),
    ]
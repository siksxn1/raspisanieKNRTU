# Generated by Django 4.1.7 on 2023-05-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_alter_lesson_participants_id_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson_participants',
            name='id_lesson',
            field=models.UUIDField(),
        ),
    ]

from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=40, blank=False, default="")
    name = models.CharField(max_length=40, blank=False, default="")
    patronic = models.CharField(max_length=40, blank=False, default="", null=True)
    id_group = models.CharField(max_length=40, blank=False, default="")
    student_book_number = models.CharField(max_length=40, blank=False, default="")

class Student_Phones(models.Model):
    phone = models.CharField(max_length=20, blank=False, default="")
    id_student = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    surname = models.CharField(max_length=40, blank=False, default="")
    name = models.CharField(max_length=40, blank=False, default="")
    patronic = models.CharField(max_length=40, blank=False, default="", null=True)

class Teacher_Phones(models.Model):
    phone = models.CharField(max_length=20, blank=False, default="")
    id_teacher = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Classes_room(models.Model):
    number = models.CharField(max_length=20, blank=False, default="")
    id_build = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class email_teacher(models.Model):
    email = models.CharField(max_length=20, blank=False, default="")
    id_teacher = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year_of_admission = models.CharField(max_length=40, blank=False, default="")
    id_headman = models.CharField(max_length=50, blank=False, default="")
    group_number = models.CharField(max_length=40, blank=False, default="", null=True)
    direction_information = models.CharField(max_length=40, blank=False, default="")

class discipline(models.Model):
    department = models.CharField(max_length=20, blank=False, default="")
    name_of_discipline = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class type_of_lessons(models.Model):
    type_of_lessons = models.CharField(max_length=50, blank=False, default="")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_participation = models.CharField(max_length=50, blank=False, default="")
    id_teacher = models.CharField(max_length=50, blank=False, default="")
    id_discipline = models.CharField(max_length=50, blank=False, default="")
    id_audience = models.CharField(max_length=50, blank=False, default="")
    date_and_time = models.CharField(max_length=40, blank=False, default="")    #не уверен что тут именно так пишется тип данных
    id_type_of_lesson = models.CharField(max_length=50, blank=False, default="")

class Build(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=40, blank=False, default="")
    city = models.CharField(max_length=40, blank=False, default="")
    street = models.CharField(max_length=40, blank=False, default="")
    house = models.CharField(max_length=40, blank=False, default="")

class Lesson_participants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_group = models.CharField(max_length=50, blank=False, default="")
from rest_framework import serializers 
import timetable.models as tt_models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Student
        fields = ('id',            
                  'surname',
                  'name',
                  'patronic',
                  'id_group',
                  'student_book_number')


class Student_PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Student_Phones
        fields = ('id',            
                  'phone',
                  'id_student',)
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Teacher
        fields = ('id',            
                  'surname',
                  'name',
                  'patronic',)
        

class Teacher_PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Teacher_Phones
        fields = ('id',            
                  'phone',
                  'id_teacher',)
        

class Classes_roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Classes_room
        fields = ('id',            
                  'number',
                  'id_build',)
        

class email_teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.email_teacher
        fields = ('id',            
                  'email',
                  'id_teacher',)
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Group
        fields = ('id',            
                  'year_of_admission',
                  'id_headman',
                  'direction_information',
                  'group_number',)
        

class disciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.discipline
        fields = ('id',            
                  'department',
                  'name_of_discipline',)
        

class type_of_lessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.type_of_lessons
        fields = ('id',            
                  'type_of_lessons',)
        

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Lesson
        fields = ('id',            
                  'id_participation',
                  'id_teacher',
                  'id_discipline',
                  'date_and_time',
                  'id_type_of_lesson',
                  'id_audience',)
        

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Build
        fields = ('id',            
                  'body',
                  'city',
                  'street',
                  'house',)
        


class Lesson_participantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tt_models.Lesson_participants
        fields = ('id',            
                  'id_group',)

from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializer import *

from django.http import JsonResponse
import json

@api_view(["GET"])
def get_student_by_id(request):
    student_id = request.GET['id']

    student = Student.objects.get(id=student_id)

    return JsonResponse({
        'Surname': student.surname
    }, status=200)
  
@api_view(['GET'])
# Пишем любое название вашей функции.
# Устанавливаем метод, по которому будет идти доступ.
def getAllStudents(request):
    # Получаем все объекты.
    students = Student.objects.all()

    # Получаем преоьбразованный формат
    srlz = StudentSerializer(students, many=True)

    # Отдаем данные в ответ на запрос.
    return Response(srlz.data)
# Create your views here.


@api_view(['POST'])
def add_student(request):
    try:
        data = json.loads(request.body.decode())
        student_id = uuid.uuid4()

        Student.objects.create(
            id = student_id,
            surname = data["surname"],
            name = data["name"],
            patronic = data["patronic"],
            student_book_number=data["student_book_number"]
            )
            #спросить про номер группы, т.е. id группы

        return JsonResponse({
            'id': student_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400) #узнать почему ошибка


    return Response()


@api_view(['POST'])
def add_teacher(request):
    try:
        data = json.loads(request.body.decode())
        teacher_id = uuid.uuid4()

        Teacher.objects.create(
            id = teacher_id,
            surname = data["surname"],
            name = data["name"],
            patronic = data["patronic"],
            )


        return JsonResponse({
            'id': teacher_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400) #узнать почему ошибка


    return Response()
@api_view(['GET'])
def find_group_by_number(request):
    groupnumb=request.GET["number"]
    group=Group.objects.get(group_number=groupnumb)
    return JsonResponse({
        'responce': "запрос прошёл",
        'id': group.id
    })

@api_view(['POST'])
def add_group(request):
    try:
        data = json.loads(request.body.decode())
        group_id = uuid.uuid4()

        Group.objects.create(
            id = group_id,
            year_of_admission = data["year_of_admission"],
            group_number = data["group_number"],
            direction_information = data["direction_information"]
            )
        return JsonResponse({
            'id': group_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400) #узнать почему ошибка


    return Response()

@api_view(['POST'])
def add_group(request):
    try:
        data = json.loads(request.body.decode())
        group_id = uuid.uuid4()

        Group.objects.create(
            id = group_id,
            year_of_admission = data["year_of_admission"],
            group_number = data["group_number"],
            direction_information = data["direction_information"]
            )
        return JsonResponse({
            'id': group_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400) #узнать почему ошибка


    return Response()

@api_view(['GET'])
def get_timetable_for_group(request):
    groupnumb = request.GET["number"]
    group = Group.objects.get(group_number=groupnumb)
    participants = Lesson_participants.objects.filter(group_number=group.id)
    lessons = Lesson.object.filter(id_participation=participants.id)
    ser = LessonSerializer(data=lessons, many=True)
    return Response(data=ser.data)

    #return JsonResponse({
        #'responce': "запрос прошёл",
        #'id': group.id,
        #'id_participation': participants.id,
        #'id_teacher': Teacher.id,
        #'id_discipline': discipline.id,
        #'id_audience':












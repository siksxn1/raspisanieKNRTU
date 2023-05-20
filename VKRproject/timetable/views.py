
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
def find_student_by_id(request):
    student_id = request.GET['id']
    student = Student.objects.get(id=student_id)

    return JsonResponse({
        'Surname': student.surname
    }, status=200)
  
@api_view(['GET'])
def getAllStudents(request):
    students = Student.objects.all()

    srlz = StudentSerializer(students, many=True)

    # Отдаем данные в ответ на запрос.
    return Response(srlz.data)



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
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)


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
    #srlz=GroupSerializer(group)


    return  JsonResponse({
        'responce': "запрос прошёл",
        'id': group.id,
        'year_of_admission': group.year_of_admission,
        'headman': group.id_headman
    })

@api_view(['GET'])
def find_headman_by_number_of_group(request):
    try:
        groupnumb=request.GET["number"]

        group=Group.objects.get(group_number=groupnumb)
    
        headman_id = group.id_headman

        headman = Student.objects.get(id = headman_id)

        phones = Student_Phones.objects.filter(id_student = headman_id)

        phone_list: list = []

        for phone in phones:
            phone_list.append(phone.phone)

        student = {
            "Surname": headman.surname,
            "Name": headman.name,
            "Patronic": headman.patronic,
            "Group": group.group_number,
            "Phones": phone_list
        }

        return JsonResponse(data=student,safe=False)
    except Exception as error:
        return JsonResponse({
            "Error": f'{error}',
            "ErrorType": f'{type(error)}'
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
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)

    return Response()

@api_view(['POST'])
def add_discipline(request):
    try:
        data = json.loads(request.body.decode())
        discipline_id = uuid.uuid4()

        discipline.objects.create(
            id = discipline_id,
            name_of_discipline = data["name_of_discipline"],
            department = data["department"],
            )
        return JsonResponse({
            'id': discipline_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()


@api_view(['POST'])
def add_Student_Phones(request):
    try:
        data = json.loads(request.body.decode())
        Student_Phones_id = uuid.uuid4()

        Student_Phones.objects.create(
            id = Student_Phones_id,
            phone = data["phone"],
            id_student = data["id_student"],
            )
        return JsonResponse({
            'id': Student_Phones_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()


@api_view(['POST'])
def add_Classes_room(request):
    try:
        data = json.loads(request.body.decode())
        Classes_room_id = uuid.uuid4()

        Classes_room.objects.create(
            id = Classes_room_id,
            number = data["number"]
            )
        return JsonResponse({
            'id': Classes_room_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()

@api_view(['POST'])
def add_type_of_lessons(request):
    try:
        data = json.loads(request.body.decode())
        type_of_lessons_id = uuid.uuid4()

        type_of_lessons.objects.create(
            id = type_of_lessons_id,
            type_of_lessons = data["type_of_lessons"]
            )
        return JsonResponse({
            'id': type_of_lessons_id
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()



@api_view(['POST'])
def update_students_data(request):
    try:
        data = json.loads(request.body.decode())
        student = Student.objects.get(id=data["id"])

        student.surname = data["surname"]
        student.name = data["name"]
        student.patronic = data["patronic"]
        student.id_group = data["id_group"]
        student.student_book_number = data["student_book_number"]


        student.save()
        return JsonResponse({
            'responce': "Данные студента успешно обновлены"
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()


@api_view(['POST'])
def update_groups_data(request):
    try:
        data = json.loads(request.body.decode())
        group = Group.objects.get(group_number=data["group_number"])

        group.year_of_admission = data["year_of_admission"]
        group.id_headman = data["id_headman"]
        group.direction_information = data["direction_information"]

        group.save()
        return JsonResponse({
            'responce': "Данные группы успешно обновлены"
        })
    except Exception as error:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400)
    return Response()



@api_view(['GET'])
def get_timetable_for_group(request):
    groupnumb = request.GET["number"]
    group = Group.objects.get(group_number=groupnumb)

    participations = Lesson_participants.objects.filter(id_group = group.id)

    lessons: list = []

    time_table: list = []

    for participation in participations:
            lessons.append(Lesson.objects.filter(id=participation.id_lesson))

def get_lesspns_for_day(day: Lesson_time, lessons: list[Lesson]):
    day_lessons: list = []

    for lesson in lessons:
        if lesson.date_and_time == day:
            day_lessons.append({
                "Lesson": get_discipline_by_id(lesson.id_discipline).name_of_discipline,
                "Type": get_lesson_type(lesson.id_type_of_lesson).type_of_lessons,
                "Teacher": f'{Teacher.objects.get(id=lesson.id_teacher).surname} {Teacher.objects.get(id=lesson.id_teacher).name}',
                "Audence": Classes_room.objects.get(id=lesson.id_audience),
            })

    return day_lessons


def get_discipline_by_id(discipline_id) -> discipline:
    return discipline.objects.get(id=discipline_id)

def get_lesson_type(type_id) -> type_of_lessons:
    return type_of_lessons.objects.get(id=type_id)

    #return JsonResponse({
        #'responce': "запрос прошёл",
        #'id': group.id,
        #'id_participation': participants.id,
        #'id_teacher': Teacher.id,
        #'id_discipline': discipline.id,
        #'id_audience':












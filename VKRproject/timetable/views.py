
from rest_framework.response import Response
from rest_framework.decorators import api_view
=======
import uuid

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Student
from .serializer import StudentSerializer

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
            name = data['"name'],
            patronic = data["patronic"],
            studend_book_number = data["studend_book_number"])
            #спросить про номер группы, т.е. id группы

        return JsonResponse({
            'id': student_id
        })
 
    except:
        return JsonResponse({'error': 'Произошла ошибка во время выполнения запроса'}, status = 400) #узнать почему ошибка 

    return Response()
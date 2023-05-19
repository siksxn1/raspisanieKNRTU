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

# Create your views here.

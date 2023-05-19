from timetable import views
from django.urls import path, include

urlpatterns = [
    path('allstudents/', views.getAllStudents),
    path('student/add', views.add_student)
        
]
from timetable import views
from django.urls import path, include, re_path

urlpatterns = [
    path('allstudents/', views.getAllStudents),

    path('student/add', views.add_student),
    path('teacher/add', views.add_teacher),
    path('group/add', views.add_group),
    re_path(r'group/find/$', views.find_group_by_number),
    re_path(r'student/find/$', views.find_student_by_id)

        
]
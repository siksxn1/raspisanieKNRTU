from timetable import views
from django.urls import path, include, re_path

urlpatterns = [
    path('allstudents/', views.getAllStudents),
    path('student/add', views.add_student),
    path('teacher/add', views.add_teacher),
    re_path(r'group/find/$', views.find_group_by_number),
    path('group/add', views.add_group)
        
]
from timetable import views
from django.urls import path, include, re_path

urlpatterns = [
    path('allstudents/', views.getAllStudents),
    path('student/add', views.add_student),
    path('teacher/add', views.add_teacher),
    path('group/add', views.add_group),
    path('discipline/add', views.add_discipline),
    path('audience/add', views.add_Classes_room),
    path('lesson/add', views.add_lesson),
    path('lesson_participants/add', views.add_lesson_participants),
    path('build/add', views.add_build),
    path('phonesheadman/add', views.add_Student_Phones),
    path('type_of_lessons/add', views.add_type_of_lessons),
    path('students/update', views.update_students_data),
    path('groups/update', views.update_groups_data),
    path('lesson_participants/update', views.update_lesson_participants_data),
    re_path(r'group/find/$', views.find_group_by_number),
    re_path(r'student/find/$', views.find_student_by_id),
    re_path(r'headman/find/$', views.find_headman_by_number_of_group),
    re_path(r'gettimetable$', views.get_timetable_for_group),

    # Secure method.
    #path("/createLessonTime", views.create_lesson_times)
]
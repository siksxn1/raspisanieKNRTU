from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('timetable/', include('timetable.urls'), name='timetable'),
]

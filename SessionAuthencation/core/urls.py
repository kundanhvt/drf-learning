from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/',views.StudentAPI.as_view()),
    path('student_api/<int:id>/',views.StudentAPI.as_view()),
    path('auth/',include('rest_framework.urls', namespace='rest_framework'))
]

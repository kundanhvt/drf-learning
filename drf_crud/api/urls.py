from django.urls import path
from api import views

urlpatterns = [
    path('studentapi',views.student_api),
]


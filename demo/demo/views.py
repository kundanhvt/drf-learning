from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.

def home(request):
    text = ''
    obj = Student.objects.all()
    for stu in obj:
        text += '<p>'+stu.name+'</p>'
    return HttpResponse(text)

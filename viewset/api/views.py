from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data)

    def retrieve(self,request,pk = None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
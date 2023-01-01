from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student

@api_view()
def home(request):
    return Response({'msg','Hello World'})

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == 'GET':
        id = request.data.get('id')
        print(request.data)
        if id is not None:
            obj = Student.objects.get(id=id)
            serializer = StudentSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Student.objects.all()
            serializer = StudentSerializer(objs,many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data':'Data Created'})
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
 
    if request.method == 'DELETE':
        id = request.data.get('id')
        obj = Student.objects.get(id=id)
        obj.delete()
        return Response({'msg':'Data Deleted'})
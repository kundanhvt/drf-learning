from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework import status


class StudentAPI(APIView):
    def get(self,request,id = None,format = None):
        if id is not None:
            obj = Student.objects.get(id=id)
            serializer = StudentSerializer(obj)
            return Response(serializer.data)
        else:
            objs = Student.objects.all()
            serializer = StudentSerializer(objs,many=True)
            return Response(serializer.data)

    def post(self,request,format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id,format=None):
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id,format=None):
        obj = Student.objects.get(id=id)
        obj.delete()
        return Response({'msg':'Data Deleted'})

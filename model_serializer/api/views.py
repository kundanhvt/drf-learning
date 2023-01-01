from django.shortcuts import render
from django.views import View
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request, *args,**kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json = JSONRenderer().render(serializer.data)
            return HttpResponse(json, content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json = JSONRenderer().render(serializer.data)
        return HttpResponse(json, content_type='application/json')

    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer =StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res ={
                'msg':'Data Created'
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')

    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type ='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type ='application/json')

    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')

        
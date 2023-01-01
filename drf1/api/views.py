from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt



def studen_details(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data, safe=True)

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(data = serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')



@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg':"Data Created"
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type="application/json")
    return HttpResponse('get request')
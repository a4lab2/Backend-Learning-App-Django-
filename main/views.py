from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializer import TeacherSerializer
from . import models
from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.clc

# class TeacherList(APIView):
#     def get(self,request):
#         teachers=models.Teacher.objects.all()
#         serializer=TeacherSerializer(teachers,many=True)
#         return Response(serializer.data)
    
class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]
   

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]
   
@csrf_exempt
def teacher_login(request):
    email = request.POST.get('email')
    password=request.POST.get('password')
    # print(request.POST)
    teacherData=models.Teacher.objects.get(email=email,password=password)
    if teacherData:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})

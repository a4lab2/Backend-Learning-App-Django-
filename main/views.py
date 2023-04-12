from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import TeacherSerializer
from . import models
from rest_framework.response import Response
# Create your views here.clc

# class TeacherList(APIView):
#     def get(self,request):
#         teachers=models.Teacher.objects.all()
#         serializer=TeacherSerializer(teachers,many=True)
#         return Response(serializer.data)
    
class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
   

class TeacherList(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
   
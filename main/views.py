from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializer import TeacherSerializer,CategorySerializer,CourseSerializer,ChapterSerializer
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
    
    teacherData=models.Teacher.objects.get(email=email,password=password)
    # return HttpResponse(teacherData.email)
    if teacherData:
        return JsonResponse({'bool':True,'teacher_id':teacherData.id})
    else:
        return JsonResponse({'bool':False})




class CategoryList(generics.ListCreateAPIView):
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[permissions.IsAuthenticated]
   



class CourseList(generics.ListCreateAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]
   

class TeacherCourseList(generics.ListAPIView):
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)
    
   


class ChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer
    # permission_classes=[permissions.IsAuthenticated]
   

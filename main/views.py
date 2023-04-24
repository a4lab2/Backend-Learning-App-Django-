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
    try:
        teacherData=models.Teacher.objects.get(email=email,password=password)
    except:
        teacherData=None
    
    if teacherData:
        return JsonResponse({'bool':True,'teacher_id':teacherData.id})
    else:
        return JsonResponse({'bool':False})


class CategoryList(generics.ListCreateAPIView):
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer
    # permission_classes=[permissions.IsAuthenticated]
   



class CourseList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        result = self.request.GET.get('result')
        if result:
            qs = qs.order_by('-id')[:int(result)]
        
        if 'category' in self.request.GET:
            category=self.request.GET['category']
            qs=models.Course.objects.filter(techs__icontains=category)

        return qs
    


   

class TeacherCourseList(generics.ListAPIView):
    serializer_class=CourseSerializer
    # permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return models.Course.objects.filter(teacher=teacher)
    
   
class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    
    

class CourseDetailView(generics.RetrieveAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
    
    

class ChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer
    # permission_classes=[permissions.IsAuthenticated]
   


class CourseChapterList(generics.ListAPIView):
    
    serializer_class=ChapterSerializer
    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)
    
   
class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer
    # permission_classes=[permissions.IsAuthenticated]
   
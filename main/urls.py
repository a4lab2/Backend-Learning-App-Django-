from django.urls import path

from . import views

urlpatterns = [
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherList.as_view()),
    path('teacher-login', views.teacher_login),



    path('category/', views.CategoryList.as_view()),
]
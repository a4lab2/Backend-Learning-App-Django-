from django.db import models
from django.core import serializers
# Create your models here.
class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    detail=models.TextField(null=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    skills=models.TextField()

    class Meta:
        verbose_name_plural = ("Teachers")




# Create your models here.
class CourseCategory(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    class Meta:
        verbose_name_plural = ("Course Categories")

    def __str__(self):
        return self.title


# Create your models here.
class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher_courses')
    title=models.CharField(max_length=100)
    description=models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/',null=True)
    techs=models.TextField(null=True)

    class Meta:
        verbose_name_plural = ("Courses")

    def related_videos(self):
        related_videos=Course.objects.filter(techs__icontains=self.techs)
        return serializers.serialize('json',related_videos)

    def tech_list(self):
        tech_list=self.techs.split(',')
        return tech_list
        


# Create your models here.
class Chapter(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='course_chapters')
    title=models.CharField(max_length=100)
    description=models.TextField()
    video=models.FileField(upload_to='chapter_videos/',null=True)
    remarks=models.TextField(null=True)

    class Meta:
        verbose_name_plural = ("4 Chapters")



# Create your models here.
class Student(models.Model):

    full_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    address=models.TextField()
    interested_categories=models.TextField()
    class Meta:
        verbose_name_plural = ("Students")



# class (models.Model):

    

#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})

from django.db import models

# Create your models here.
class Teacher(models.Model):

    full_name=models.CharField(max_length=100)
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


# Create your models here.
class Course(models.Model):
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField()
    class Meta:
        verbose_name_plural = ("Courses")



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

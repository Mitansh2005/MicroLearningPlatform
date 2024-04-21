from django.db import models

# Create your models here.
class Courses:
  course_name=models.CharField(max_length=150)
  course_desc=models.TextField(max_length=500)
  course_duration=models.IntegerField()
  course_image=models.ImageField()
  
  


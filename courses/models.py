from django.db import models

from register.models import CustomUser

# Create your models here.

class Department(models.Model):
    department_code = models.CharField(max_length=10, null = False)    # e.g. CSCI
    department_name = models.CharField(max_length=100, null = False)   # e.g. Computer Science


class Courses(models.Model):
    course_name = models.CharField(max_length=100, null = False)
    course_number = models.CharField(max_length=100, null = False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_description = models.CharField(max_length=1000, blank=True)
    object = models.Manager()
    #class Meta:
    #    app_label = 'courses'



class TutorTeachesCourse(models.Model):
    tutor = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to=models.Q(is_status=True))
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    object = models.Manager()

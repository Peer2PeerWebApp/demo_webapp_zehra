from django.db import models

from register.models import CustomUser

# Create your models here.


class Courses(models.Model):
    course_name = models.CharField(max_length=100, null = False)
    object = models.Manager()
    #class Meta:
    #    app_label = 'courses'


class TutorTeachesCourse(models.Model):
    tutor = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to=models.Q(is_status=True))
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

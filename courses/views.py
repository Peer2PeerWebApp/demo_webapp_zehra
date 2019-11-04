from django.shortcuts import render

from .models import Courses

# Create your views here.

def course_list(request):
    course_list = Courses.object.all()
    context = {
        'course_list': course_list
    }  
    return render(request, 'course_list.html', context)
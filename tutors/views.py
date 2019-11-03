from django.shortcuts import render
from register.models import CustomUser

# Create your views here.

def tutors_list(request):
    user_list = CustomUser.objects.all()
    context = {
        'user_list': user_list
    }  
    return render(request, 'tutors_list.html', context)
from django.shortcuts import render
from register.models import CustomUser

# Create your views here.

def tutors_list(request):
    user_list = CustomUser.objects.all()
    context = {
        'user_list': user_list
    }  
    return render(request, 'tutors_list.html', context)

def show_profile( request, user):
    user = CustomUser.objects.get(username = user)
    context = {
        'user': user
    }  
    return render(request, 'show_profile.html', context)
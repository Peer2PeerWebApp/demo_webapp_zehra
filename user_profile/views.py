from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import EditProfile, ViewProfile
from register.models import CustomUser

# Create your views here.

#def manage_profile(request):
#    return render(request, 'manage_profile.html')

'''
def view_profile(request):
    args = {}

    if request.method == 'POST':
        form = ViewProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('%s'%(reverse('home')))
    else:
        form = ViewProfile()

    args['form'] = form
    return render(request, 'view_profile.html', args)
'''

@login_required
def view_profile(request):
    profile = CustomUser.objects.get(username=request.user)
    context = {
        'profile': profile
    }  
    return render(request, 'view_profile.html', context)

def edit_profile(request):
    args = {}

    if request.method == 'POST':
        form = EditProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('%s'%(reverse('view_profile')))
    else:
        form = EditProfile()

    args['form'] = form
    return render(request, 'edit_profile.html', args)
from django.shortcuts import render, redirect, reverse
from .forms import ViewProfile

# Create your views here.

#def manage_profile(request):
#    return render(request, 'manage_profile.html')


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
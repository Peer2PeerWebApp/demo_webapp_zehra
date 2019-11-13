"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

#apps
from register import views as reg_v
from user_profile import views as prof_v
from tutors import views as tutors_v

#framework
from django_messages import views as messages_v


urlpatterns = [
    #path('admin/', admin.site.urls),
    
    path('', reg_v.home, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', reg_v.register, name='register'),

    path('view_profile/', prof_v.view_profile, name='view_profile'),
    path('edit_profile/', prof_v.edit_profile, name='edit_profile'),
    path('tutors/', tutors_v.tutors_list, name='tutors_list'),

    path('show_profile/<user>/', tutors_v.show_profile, name='show_profile'),

    #path('messages/', include('postman.urls')),
    
    path('depr_messages/', include('django_messages.urls')),

    path('messages/inbox/', messages_v.inbox, {'template_name': 'my_inbox.html',}, name='messages_inbox'),
    path('messages/compose/', messages_v.compose, {'template_name': 'my_compose.html',}, name='messages_compose'),
    path('messages/outbox/', messages_v.outbox, {'template_name': 'my_outbox.html',}, name='messages_outbox'),
    path('messages/trash/', messages_v.trash, {'template_name': 'my_trash.html',}, name='messages_trash')

]

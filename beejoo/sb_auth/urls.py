# -*- coding: utf-8 -*-
from django.conf.urls import url

from django.contrib.auth.views import login, logout_then_login
from django.views.generic import CreateView

from sb_auth.forms import CustomUserCreation

urlpatterns = [
    url(r'^login/', login, {
        'template_name': 'sb_auth/login.html'
    }, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^register/', CreateView.as_view(
        template_name='sb_auth/register.html',
        form_class=CustomUserCreation,
        success_url='/'
    ), name='register')
]
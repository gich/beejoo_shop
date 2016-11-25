# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from sb_auth.models import CustomUser

__author__ = 'gia_sebua'

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
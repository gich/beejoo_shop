from django import forms
from django.core.exceptions import ValidationError

from sonic_beejoo.models import *


class DesignTypeForm(forms.ModelForm):
    class Meta:
        model = DesignType
        fields = [ 'full', ]

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = [ 'full',]
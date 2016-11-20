from django import forms
from django.core.exceptions import ValidationError

from sonic_beejoo.models import *


class DesignTypeForm(forms.ModelForm):
    class Meta:
        model = DesignType
        fields = '__all__'

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = '__all__'
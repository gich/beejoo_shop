from django import forms
from django.core.exceptions import ValidationError

from sonic_beejoo.models import *


class DesignTypeForm(forms.ModelForm):


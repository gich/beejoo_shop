from django import forms
from django.core.exceptions import ValidationError

from sonic_beejoo.models import DesignType, Good, Category, Color


class DesignTypeForm(forms.ModelForm):
    class Meta:
        model = DesignType
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = "__all__"

class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        fields = '__all__'
from django import forms
from . import models
class CategoryForms(forms.ModelForm):
    class Meta:
        model = models.CategoryModel
        fields = '__all__'
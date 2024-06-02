from django import forms
from . import models
class TaskForms(forms.ModelForm):
    class Meta:
        model = models.TaskModel
        fields = '__all__'
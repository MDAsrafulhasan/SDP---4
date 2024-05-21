from django import forms
# from frist_app.models import StudentModel
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels = {
            'name ': 'Student Name',
            'roll' : 'Student Roll'
        }

        widgets = {
            'name': forms.TextInput()
        }
        help_texts = {
            'name': 'Enter Student Name',
            'roll': 'Enter Student Roll'
        }
        error_messages = {
            'name': {
                'max_length': 'Name is too long',
                'required': 'Name is required'
                }
            }
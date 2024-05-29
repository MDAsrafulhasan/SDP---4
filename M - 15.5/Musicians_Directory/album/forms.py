from django import forms
from . import models

class AlbunForm(forms.ModelForm):
    class Meta:
        model = models.AlbumModel
        fields = '__all__'

from django import forms
from django.forms.widgets import *
import datetime
from . import models

class PracticeForm(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # comment = forms.CharField(widget=forms.Textarea)
    # comment = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    # agree = forms.BooleanField()
    # date = forms.DateField()
    # birthdate = forms.DateField(widget=NumberInput(attrs = {'type':'date'}))

    # Birth_Year = ['2000','2010','2030']
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=Birth_Year))

    # value = forms.DecimalField()

    # email_address = forms.EmailField( 
    # required = False,)

    # message = forms.CharField()
    # email = forms.EmailField(label = "Please enter your email address")
    # First_name = forms.CharField(initial='your name')
    # agree = forms.BooleanField(initial=True)
    # day = forms.DateField(initial=datetime.date.today)

    # F_choice = [
    #     ('blue','Blue'),
    #     ('green','Green'),
    #     ('red','Red')
    # ] 
    # choice = forms.ChoiceField(choices=F_choice)
    # choice = forms.ChoiceField(widget=forms.RadioSelect,choices=F_choice)
    # choice = forms.MultipleChoiceField(choices=F_choice)
    # choice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=F_choice)
    # title = forms.CharField()
    # description = forms.CharField()
    # first_name = forms.CharField(max_length=200)
    # last_name = forms.CharField(max_length=200)
    # roll = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())



class ModelForm(forms.ModelForm):
    class Meta:
        model = models.PracticeModels
        fields = '__all__'
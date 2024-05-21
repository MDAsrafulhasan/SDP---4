from django import forms

from django.core import validators


# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label='User name: ',help_text="total length must be 40 character", required=False , disabled=True, widget=forms.Textarea(attrs={'id':'text_area','class':'class1 class2','placeholder':'Enter your name...'}))
    # file = forms.FileField()
    email = forms.EmailField(label='User email')
    # Age = forms.IntegerField(label='Age')
    Age = forms.IntegerField(label='Age',widget=forms.NumberInput)
    Weight = forms.FloatField(label='weight')
    Balance = forms.DecimalField(label='balance')
    Check = forms.BooleanField(label='check')
    # birthday = forms.DateField(label='birthday')
    birthday = forms.CharField(label='birthday',widget= forms.DateInput(attrs= {'type':'date'}))
    # Appointment = forms.DateTimeField(label='appointment')
    Appointment = forms.CharField(label='appointment',widget= forms.DateInput(attrs= {'type':'datetime-local'}))
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')] 
    size = forms.ChoiceField(choices= CHOICES,widget=forms.RadioSelect)
    meal = [('P','Pepperoni'),('M','Masroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)



# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
        # if len(valname) < 10:
        #     raise forms.ValidationError('Please enter a valid name with at least 10 characters')
        # else:
        #     return valname
        
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
        # if '.com' not in valemail:
        #     raise forms.ValidationError('Please enter a valid email address. There is no .com in the email address')
        # else:
        #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Please enter a valid name with at least 10 characters')

    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Please enter a valid email address. There is no .com in the email address')



def length_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Please enter a value with at least 10 characters')


class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message='Please enter a valid name with maximum 10 characters')])

    text = forms.CharField(widget=forms.TextInput,validators=[length_check])

    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34,message='age must be maximum 34'),validators.MinValueValidator(24,message='age at least 24')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','jpg'],message='file must be .pdf')])


class PasswordValidationProject(forms.Form):
    name  = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']

        if val_pass != val_con_pass:
            raise forms.ValidationError('password and confirm password must be same')
        if len(val_name) < 15:
            raise forms.ValidationError('Please enter a valid name with at least 15 characters')
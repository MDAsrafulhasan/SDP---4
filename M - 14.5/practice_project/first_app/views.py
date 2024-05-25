from django.shortcuts import render
from . import forms

def home(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'home.html', {'name':name , 'email':email} )
    else:
        return render(request, 'home.html' )
    # return render(request, 'home.html')

def practice(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'practice.html', {'name':name , 'email':email} )
    else:
        return render(request, 'practice.html' )

def PracticeFormApi(request):
    if request.method == 'POST':
        form = forms.PracticeForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request,'D_form_api.html', {'form':form , 'name':name, 'email':email})
    else:
        form = forms.PracticeForm()
        return render(request,'D_form_api.html', {'form':form})


def PracticeModelApi(request):
    model = forms.ModelForm()
    return render(request,'D_model_api.html',{'model' : model})
    # if request.method == 'POST':
    #     model = forms.ModelForm
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     return render(request,'D_model_api.html', {'model':model , 'name':name, 'email':email})
    # else:
    #     model = models.PracticeModels()
    #     return render(request,'D_model_api.html', {'model':model})
    

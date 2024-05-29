from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def MusicianView(request):
    # musician_form = forms.MusicianForm()
    # return render(request,'musician.html',{'musician_form':musician_form})
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            # return redirect('musician_page')
            return redirect('table_page')
        
    else:
        musician_form = forms.MusicianForm()
    return render(request,'musician.html',{'musician_form':musician_form})


def EditMusicianView(request,id):
    musician_id = models.MusicianModel.objects.get(pk=id)
    musician_form = forms.MusicianForm(instance=musician_id)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician_id)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('table_page')

    return render(request,'musician.html',{'musician_form':musician_form})
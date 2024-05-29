from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models
def AlbumViews(request):
    # albumform = forms.AlbunForm()
    # return render(request, 'album.html', {'album_form': albumform})
    if request.method=='POST':
        albumform = forms.AlbunForm(request.POST)
        if albumform.is_valid():
            albumform.save()
            # return redirect('album_page')
            return redirect('table_page')
    else:
        albumform = forms.AlbunForm()
    return render(request,'album.html',{'album_form':albumform})



def EditAlbumViews(request,id):
    albumid = models.AlbumModel.objects.get(pk=id)
    albumform = forms.AlbunForm(instance=albumid)
    if request.method=='POST':
        albumform = forms.AlbunForm(request.POST,instance=albumid)
        if albumform.is_valid():
            albumform.save()
            return redirect('table_page')

    return render(request,'album.html',{'album_form':albumform})

def Delete_Album(request,id):
    albumid = models.AlbumModel.objects.get(pk=id)
    albumid.delete()
    return redirect('table_page')




from django.shortcuts import render
from album.models import AlbumModel
def home(request):
    return render(request, 'base.html')

def table(request):
    datas = AlbumModel.objects.all()
    # print(datas)
    return render(request, 'table.html' , {'datas': datas})
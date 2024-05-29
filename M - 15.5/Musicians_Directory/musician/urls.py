
from django.urls import path,include
from . import views
urlpatterns = [
    path('creat_musician/', views.MusicianView , name = "musician_page"),
    path('edit_musician/<int:id>', views.EditMusicianView , name = "edit_musician"),
]


from django.urls import path,include
from . import views
urlpatterns = [
    path('creat_album/', views.AlbumViews , name = "album_page"),
    path('edit/<int:id>', views.EditAlbumViews , name = "edit_album"),
    path('delete/<int:id>', views.Delete_Album , name = "delete_album"),
]

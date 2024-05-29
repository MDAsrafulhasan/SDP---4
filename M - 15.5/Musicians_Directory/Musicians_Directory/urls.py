
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name= 'home_page'),
    path('album/', include("album.urls")),
    path('musician/', include("musician.urls")),
    path('table_form/',views.table,name = 'table_page' ),
]


from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.TaskViews , name = 'add_task_page'),
    path('edit/<int:id>', views.EditTask , name = 'edit_task_page'),
    path('delete/<int:id>', views.DeleteTask , name = 'delete_task_page'),
]

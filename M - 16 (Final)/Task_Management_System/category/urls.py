from django.urls import path,include
from . import views
urlpatterns = [
    path('add/', views.CategoryViews, name = 'add_category_page'),

]

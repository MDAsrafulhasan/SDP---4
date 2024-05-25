from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'homepage' ),
    path('practice/',views.practice, name = 'practicePage' ),
    path('Form_Api_practice/',views.PracticeFormApi , name = 'FormApi' ),
    path('Model_Api_practice/',views.PracticeModelApi , name = 'ModelApi' ),
]

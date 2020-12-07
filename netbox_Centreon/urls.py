from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.RandomAnimalView.as_view(), name='random_animal'),
]
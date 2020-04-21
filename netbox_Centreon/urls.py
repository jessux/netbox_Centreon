from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.CentreonObjectStatusView.as_view(), name='CentreonObjectStatus'),
]
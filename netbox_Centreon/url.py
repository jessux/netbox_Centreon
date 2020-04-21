from django.urls import path
from . import views

urlpatterns = [
    path('centreon/', views.CentreonObjectStatus.as_view(), name='CentreonObjectStatus'),
]
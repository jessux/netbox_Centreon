from django.shortcuts import render
from django.views.generic import View
from .models import CentreonObjectStatus

class CentreonObjectStatusView(View):

    def get(self, request):
        CentreonObjects = CentreonObjectStatus.objects.all()
        return render(request, 'netbox_Centreon/CentreonObjectStatus.html', {
            'CentreonObjects': CentreonObjects,
        })
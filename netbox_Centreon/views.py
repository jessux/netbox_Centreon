from django.shortcuts import render
from django.views.generic import View
from .models import CentreonObjectStatus

class CentreonObjectStatusView(View):

    def get(self, request):
        CentreonObject = CentreonObjectStatus.objects.order_by('?').first()
        return render(request, 'netbox_Centreon/CentreonObjectStatus.html', {
            'CentreonObject': CentreonObject,
        })
from django.shortcuts import render
from django.views.generic import View
from .models import CentreonObjectStatus

class RandomCentreonView(View):

    def get(self, request):
        Centreon = CentreonObjectStatus.objects.order_by('?').first()
        return render(request, 'netbox_Centreon/templates/netbox_Centreon/CentreonObjectStatus.html', {
            'CentreonObjects': Centreon,
        })
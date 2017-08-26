from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from analyser.models import Item
from django.http import HttpResponse
from django.http import JsonResponse

import logging


# Create your views here.
def index(request):
    context = {'items': Item.objects.filter(item_name='Sugar'),
               'recommendations': ['Wafer', 'Namkeen'],
               }
    return render(request, 'analyser/index.html', context)


def seller_home(request):
    return render(request, 'analyser/home.html', {})


@csrf_exempt
def addItem(request):
    logging.error("IN")
    if request.is_ajax():
        request_data = request.POST
        logging.error(request_data['newItem'])
        data = {}
        data['price'] = Item.objects.filter(item_name=request_data['newItem'])[0].price
        data['recommend'] = 'Soap'
    return JsonResponse(data)

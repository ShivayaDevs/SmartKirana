from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from analyser.models import Item
from django.http import HttpResponse
from django.http import JsonResponse

from mlutils import recommender
import logging

# Opens the customer's billing page in front of shopkeeper.
def index(request):
    context = {'items': Item.objects.filter(item_name='Sugar'),
               'recommendations': ['Wafer', 'Namkeen'],
               }
    return render(request, 'analyser/index.html', context)


# Used to add item to customer's bill. Also, it triggers recommendations to the shopkeeper.
@csrf_exempt
def addItem(request):
    if request.is_ajax():
        request_data = request.POST
        logging.error(request_data['newItem'])
        data = {}
        data['price'] = Item.objects.filter(item_name=request_data['newItem'])[0].price
        # TODO: Replace with ML algorithm.
        data['recommend'] = recommender.find_index(request_data['newItem'])
    return JsonResponse(data)

# Seller's home page.
def seller_home(request):

    from mlutils.recommender import dictionary
    from mlutils  import time_series_predictor

    context = {
        'today_income' : 5000,
        'today_expenses' : 3000,
        'today_debt' : 0.0,
        'today_credits' : 0.0,
        'week_income' : 20000,
        'week_expenses' : 18000,
        'week_debt' : 0.0,
        'week_credits' : 0.0,
        'month_income' : 50000,
        'month_expenses' : 30000,
        'month_debt' : 200.0,
        'month_credits' : 4000.0,
    }
    for i in range(0, 6):
        context['a'+str(i)] = dictionary[i] + ' will last for ' + str(time_series_predictor.predict(dictionary[i])) + ' more days'

    return render(request, 'analyser/home.html', context)

from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'items': ['Sugar', 'Tea', 'Milk'],
               'recommendations': ['Wafer', 'Namkeen'],
               }
    return render(request, 'analyser/index.html', context)

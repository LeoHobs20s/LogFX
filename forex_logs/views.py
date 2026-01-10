from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Pair
from .forms import PairForm


def index(request):
    """ This view will render the home page for LogFX """

    return render(request, 'forex_logs\index.html')


def currency_pairs(request):
    """ This view will render the currency pair page """

    pairs = Pair.objects.order_by('date_created')
    context = {'pairs':pairs}
    return render(request, 'forex_logs\pairs.html', context)


def add_pair(request):
    """ This view will render the add pair page """

    if request.method != 'POST':
        # No Data Submitted; create a blank form
        form = PairForm()
    else:
        # POST Data Submitted; process data
        form = PairForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('currency_pairs'))
    
    context = {'form':form}
    return render(request, 'forex_logs/new_pair.html', context)


def pair_price(request, pair_id):
    """ This view will render the pair's price data """

    pair = Pair.objects.get(id=pair_id)
    prices = pair.price_set.order_by('date_inserted')
    context = {'pair':pair, 'prices':prices}
    return render(request, 'forex_logs/pair_price.html', context)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Pair, Price
from .forms import PairForm, PriceForm


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

    pair = get_object_or_404(Pair, pk=pair_id)
    prices = pair.price_set.order_by('date_inserted')
    context = {'pair':pair, 'prices':prices}
    return render(request, 'forex_logs/pair_price.html', context)


def add_price(request, pair_id):
    """ This will render a page to add new currency price data """

    pair = get_object_or_404(Pair, pk=pair_id)

    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = PriceForm()
    else:
        # POST Data Submitted; process data
        form = PriceForm(data=request.POST)
        if form.is_valid():
            prices = form.save(commit=False)
            prices.pair = pair
            prices.save()
            return HttpResponseRedirect(reverse('pair_price', args=[pair_id]))
    
    return render(request, 'forex_logs/new_price.html', {'form':form, 'pair':pair})


def edit_pair(request, pair_id):
    """ This view will render the page to edit the name of the pair """

    pair = get_object_or_404(Pair, pk=pair_id)

    if request.method != 'POST':
        # Initial Request, create form with current data
        form = PairForm(instance=pair)
    else:
        # POST Request, replace current data with the new data
        form = PairForm(instance=pair, data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('currency_pairs'))
        
    context = {'form':form, 'pair':pair}
    return render(request, 'forex_logs/edit_pair.html', context)


def delete_pair(request, pair_id):
    """ This view will run the logic code to delete the currency pair """

    pair = get_object_or_404(Pair, pk=pair_id)
    pair.delete()
    return HttpResponseRedirect(reverse('currency_pairs'))


def edit_pair_price(request, price_id):
    """ This view will render the update feature for the pair prices """

    price = get_object_or_404(Price, pk=price_id)
    pair = price.pair

    if request.method != 'POST':
        # Initial Request; create a form with current pair price data
        form = PriceForm(instance=price)
    else:
        # POST Data Submitted; replace current pair price data with post data
        form = PriceForm(instance=price, data=request.POST)

        if form.is_valid():
            updated_price = form.save(commit=False)
            updated_price.pair = pair
            updated_price.save()
            return HttpResponseRedirect(reverse('pair_price', args=[pair.id]))

    context = {'form':form, 'pair':pair, 'price':price}
    return render(request, 'forex_logs/edit_pair_price.html', context) 


def delete_pair_price(request, price_id):
    """ This view will render the feature to delete a pair price """

    price = get_object_or_404(Price, pk=price_id)
    price.delete()
    return HttpResponseRedirect(reverse('pair_price', args=[(price.pair).id]))
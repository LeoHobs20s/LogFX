""" Defines URL patterns for forex_logs """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currency pairs/', views.currency_pairs, name='currency_pairs'),
    path('add_pair/', views.add_pair, name='add_pair'),
    path('pair_price/<int:pair_id>/',views.pair_price, name='pair_price'),
]
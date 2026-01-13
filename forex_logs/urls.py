""" Defines URL patterns for forex_logs """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('currency pairs/', views.currency_pairs, name='currency_pairs'),
    path('add_pair/', views.add_pair, name='add_pair'),
    path('pair_price/<int:pair_id>/',views.pair_price, name='pair_price'),
    path('add_price/<int:pair_id>/', views.add_price, name='add_price'),
    path('edit_pair/<int:pair_id>/', views.edit_pair, name='edit_pair'),
    path('delete_pair/<int:pair_id>/', views.delete_pair, name='delete_pair'),
    path('edit_pair_price/<int:price_id>/', views.edit_pair_price, name='edit_pair_price'),
    path('confirm_delete/<int:object_id>/', views.confirm_delete, name='confirm_delete'),
    path('delete_pair_price/<int:price_id>/', views.delete_pair_price,
     name='delete_pair_price'),
]
from django.db import models
from django.contrib.auth.models import User


class Pair(models.Model):
    """ This class represents a data model for currency pair names """

    text = models.CharField(max_length=7)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Pairs'

    def __str__(self):
        return self.text
    

class Price(models.Model):
    """ This class represents the data model for price data """
    
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    price_open = models.DecimalField(max_digits=7, decimal_places=2)
    price_close = models.DecimalField(max_digits=7, decimal_places=2)
    price_high = models.DecimalField(max_digits=7, decimal_places=2)
    price_low = models.DecimalField(max_digits=7, decimal_places=2)
    note = models.CharField(max_length=150)
    date_inserted = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Prices'
    


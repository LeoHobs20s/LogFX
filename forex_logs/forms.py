from django import forms
from .models import Pair, Price


class PairForm(forms.ModelForm):
    """ This class will represent the form to add pair for the model Pair """

    class Meta:
        model = Pair
        fields = ['text']
        labels = {'text':''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w-50 text-bg-light'
            field.widget.attrs['placeholder'] = 'Enter Currency Pair (e.g USD/JPY)'


class PriceForm(forms.ModelForm):
    """ This class will create a form to input data for the prices """

    class Meta:
        model = Price
        fields = ['price_open', 'price_high', 'price_low', 'price_close']
        labels = {'price_open':'Enter Price Open', 'price_high':'Enter Price High', 'price_low':'Enter Price Low', 'price_close':'Enter Price Close'}
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control w-50 bg-light'

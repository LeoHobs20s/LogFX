from django import forms
from .models import Pair


class PairForm(forms.ModelForm):
    """ This class will represent the form to add pair for the model Pair """

    class Meta:
        model = Pair
        fields = ['text']
        labels = {'text':''}
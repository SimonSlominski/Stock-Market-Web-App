from django import forms
from .models import StockTicker

class StockTickerForm(forms.ModelForm):

    class Meta:
        model = StockTicker
        fields = ['ticker']


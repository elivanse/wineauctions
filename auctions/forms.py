from django.forms import ModelForm

from .models import *


class listing_form(ModelForm):
    class Meta:
        model = listing
        fields = ['item', 'price', 'description', 'category',  'photo']


class bid_form(ModelForm):
    class Meta:
        model = bid
        fields = ["price"]

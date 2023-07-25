from django import forms
from .models import Order


class StatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['type']



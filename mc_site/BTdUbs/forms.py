from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name', 'url',)

class timeSlotForm(forms.Form):
    order_time = forms.TimeField(widget=forms.TimeInput(format='%h:%M'))

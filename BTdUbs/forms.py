from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name', 'url',)

    order_time = forms.TimeField(widget=forms.TimeInput(format='%h:%M'))
    recommendation = forms.CharField(initial="Something Yummy")
    note = forms.CharField(widget=forms.Textarea)

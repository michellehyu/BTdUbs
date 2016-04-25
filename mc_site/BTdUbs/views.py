from django.shortcuts import render
from django.http import HttpResponse
from .forms import StoreForm

# Create your views here.
# Default Welcome Page
def welcome(request):
    return HttpResponse("Welcome to Buy the Way.")
    
# Selection Page for Buyer
def selection(request):
    form = StoreForm()
    return render(request, 'BTdUbs/selection.html', {'form': form})
#   return HttpResponse("Select your place here.")

# Confirmation Page for Buyer
def confirmation(request):
   return HttpResponse("The members have been notified")


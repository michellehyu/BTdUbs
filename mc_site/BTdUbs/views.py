from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Default Welcome Page
def welcome(request):
    return HttpResponse("Welcome to Buy the Way.")
    
# Selection Page for Buyer
def selection(request):
    return HttpResponse("Select your place here.")

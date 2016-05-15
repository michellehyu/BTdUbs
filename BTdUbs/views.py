from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import StoreForm
from django.contrib.auth.models import User

# Create your views here.
# Default Welcome Page
def welcome(request):
    return render(request, 'BTdUbs/index.html')
    
# Selection Page for Buyer
def selection(request):
    form = StoreForm()
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            daily_selection = form.save(commit=False)
            daily_selection.store_name = request.store_name
            daily_selection.url = request.url
            daily_selection.save()
            return HttpResponseRedirect(reverse())
        else:
            return HttpResponse("error")
    else:
        return render(request, 'BTdUbs/selection.html', {'form': form})

# Confirmation Page for Buyer
def confirmation(request):
    subject = 'BuyTheWay Order Today'
    user_name = request.user
    context = {
        'user': 'someone',
        'store': request.POST['store_name'],
        'name': user_name,
        'url': request.POST['url'],
        'recommendation': request.POST['recommendation'],
        'order_time': request.POST['order_time'],
        'note': request.POST['note']
        }
    message = render_to_string('BTdUbs/email/order_email.txt', context)
    print(message)
    from_email = User.objects.get(username=user_name).email
    users = User.objects.all()   
    to_list = [u.email for u in users if u.email != from_email]
    send_mail(subject,message, from_email, to_list, fail_silently=True)
    # send_mass_mail()
    return HttpResponse("The members have been notified")
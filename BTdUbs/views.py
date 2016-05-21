from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Store
from .forms import StoreForm, OrderForm
url_base = "http://btdubs.herokuapp.com/"

# Default Welcome Page
def welcome(request):
    return render(request, 'BTdUbs/index.html')
    
# Selection Page for Buyer
@login_required
def selection(request):
    form = StoreForm()
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            # save new stores/url to the database
            daily_selection = form.save(commit=False)
            daily_selection.store_name = request.POST['store_name']
            daily_selection.url = request.POST['url']
            daily_selection.save()

            # Send an email to all the users
            subject = 'BuyTheWay Order Today'
            user_name = request.user
            order_url = '{}{}{}'.format(url_base, 'BTdUbs/order/', user_name)
            context = {
                'user': 'someone',
                'store': request.POST['store_name'],
                'name': user_name,
                'url': request.POST['url'],
                'recommendation': request.POST['recommendation'],
                'order_time': request.POST['order_time'],
                'note': request.POST['note'],
                'order_url': order_url,
            }
            html_message = render_to_string('BTdUbs/email/order_reminder_email.html', context)
            message = render_to_string('BTdUbs/email/order_reminder_email.txt', context)
            print(html_message)
            print(message)
            from_email = User.objects.get(username=user_name).email
            users = User.objects.all()   
            to_list = [u.email for u in users if u.email != from_email]
            send_mail(subject,message, from_email, to_list, fail_silently=True, html_message=html_message)
            messages.success(request, "The members have successfully been notified")
    return render(request, 'BTdUbs/selection.html', {'form': form})

# Order Page
@login_required
def order(request, buyer):
    buyer_user = get_object_or_404(User, username=buyer)
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Send an email to the buyer
            subject = 'BuyTheWay Order'
            user_name = request.user
            context = {
                'user': user_name,
                'order': request.POST['order']
            }
            message = render_to_string('BTdUbs/email/place_order.txt', context)
            print(message)
            from_email = User.objects.get(username=user_name).email
            to_list = [buyer]
            send_mail(subject,message, from_email, to_list, fail_silently=True)
            messages.success(request, "Your order has been successfully mailed")
    return render(request, 'BTdUbs/order.html',{'form': form, 'buyer': buyer_user.email})
            

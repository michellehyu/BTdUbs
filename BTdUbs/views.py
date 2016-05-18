from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Store
from .forms import StoreForm

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
            # save new stores/url to the database
            daily_selection = form.save(commit=False)
            daily_selection.store_name = request.POST['store_name']
            daily_selection.url = request.POST['url']
            daily_selection.save()

            # Send an email to all the users
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
            return HttpResponse("The members have been notified")

        else:
            return render(request, 'BTdUbs/selection.html', {'form': form})
    else:
        return render(request, 'BTdUbs/selection.html', {'form': form})


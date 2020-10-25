from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import *
import random
from django.views.generic import *
from django.urls import *
from django.contrib.auth.decorators import login_required

class Wallet(ListView):
    model=Status
    template_name='core/wallets.html'
class WalletDetail(UpdateView):
    model = Status
    form_class=forms.StatusForm
    template_name = 'core/wallet_detail.html'
    success_url = reverse_lazy('adashi-admin')

class HomePageView(TemplateView):
    template_name ='core/index.html'

def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))

@login_required
def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "core/wallet.html", {"curr_user": curr_user})
@login_required
def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.MoneyTransfer.objects.get(enter_your_user_name=request.user)
            dest_user_acc_num = curr_user.enter_the_destination_account_number

            temp = curr_user # NOTE: Delete this instance once money transfer is done
            
            dest_user = models.Status.objects.get(account_number=dest_user_acc_num) # FIELD 1
            transfer_amount = curr_user.enter_the_amount_to_be_transferred_in_USD # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user) # FIELD 3

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete() # NOTE: Now deleting the instance for future money transactions

        return redirect("account_status")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "core/money_transfer.html", {"form": form})

def addMoney(request):
    return render(request, 'core/add_money.html')
@login_required
def withdraw(request):
    if request.method == "POST":
        form = forms.WithdrawForm(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.Withdraw.objects.get(email=request.user)

            temp = curr_user # NOTE: Delete this instance once money transfer is done
            transfer_amount = curr_user.amount# FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user) # FIELD 3
            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
           
            # Save the changes before redirecting
            curr_user.save()

            temp.delete() # NOTE: Now deleting the instance for future money transactions

        return redirect("account_status")
    else:
        form = forms.WithdrawForm()
    return render(request, "core/withdraw.html", {"form": form})
@login_required
def loan(request):
    return render(request, "profiles/loans.html")



class CreateAnnouncement(CreateView):
    model = Announcement
    form_class = forms.AnnouncementForm
    template_name='registration/new_announcement.html'
    success_url = reverse_lazy('adashi-admin')


class CreateNotification(CreateView):
    model = Notification
    form_class = forms.NotificationForm
    template_name='registration/new_notification.html'
    success_url = reverse_lazy('adashi-admin')

def announcements(request):
    x=Announcement.objects.all().filter(priority='High')
    y=Announcement.objects.all().filter(priority='Medium')
    z=Announcement.objects.all().filter(priority='Low')
    notifications=Notification.objects.all().filter(target=request.user)
    context={
    'x':x,
    'y':y,
    'z':z,
    'notifications':notifications
    }
    return render(request, 'registration/announcements.html', context)


def notifications(request):
    Notifications=Notification.objects.all().filter(target=request.user)
    context={
    'Notifications':Notifications
    }
    return render(request, '', context)

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from accounts.models import *
from .forms import *
from .decorators import *
from django.views.generic import (ListView, DetailView, CreateView , UpdateView, DeleteView, TemplateView) 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, f"you're welcome to ")
            return redirect('profile_update')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def profile(request):
    
    return render(request, 'registration/profile.html')

@login_required
def profileUpdate(request):
    form = ProfileUpdate(instance=request.user)
    if request.method == "POST":
        form = ProfileUpdate(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"You have successfully Updated Your Profile")
            return redirect('home')
    return render(request, 'registration/profile_update.html', {'form':form})

# @login_required
# def ProfileUpdate(request):
#     form = ProfileUpdate(instance=request.user)
#     if request.method == "POST":
#         form = ProfileUpdate(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, F"You have successfully Updated Your Profile")
#             return redirect('profile')
#     return render(request, 'registration/profile1_update.html', {'form':form})


class Verify(LoginRequiredMixin,CreateView):
    model = Verification
    form_class = VerificationForm
    template_name='registration/new_verify.html'
    success_url = reverse_lazy('thanks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Message(LoginRequiredMixin,CreateView):
    model = Contact
    form_class = ContactForm
    template_name='registration/new_message.html'
    success_url = reverse_lazy('message-sent')


class MessageList(LoginRequiredMixin,ListView):
    model = Contact
    template_name='registration/messages.html'

def thanks(request):
    return render(request, 'registration/verify_done.html')

def message_sent(request):
    return render(request, 'registration/message_sent.html')
    
class ProfileList(ListView):
    model   =   User


class ProfileDetail(DetailView):
    model   =   User



from core.models import *
from investors.models import *
from loans.models import *
from adashi.models import *

@login_required
def user_dashboard(request):
    groups=AdashiGroup.objects.all().filter(members=request.user)
    investors=Investment.objects.all().filter(user=request.user)
    loans=Loan.objects.all().filter(customer=request.user)
    calendars=Calendar.objects.all().filter(user=request.user)
    notifications=Notification.objects.all().filter(target=request.user)
    context={
    'groups':groups,
    'investors':investors,
    'loans':loans,
    'calendars':calendars,
    'notifications':notifications
    }
    return render(request, 'registration/index.html',context)

def list_users(request):
    users= User.objects.all()
    return render(request, 'registration/user_list.html', {'users':users})

def list_investors(request):
    users= User.objects.all().filter(is_investor=True)
    return render(request, 'registration/investor_list.html', {'users':users})
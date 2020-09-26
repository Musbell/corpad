from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import *
from .forms import *
from accounts.models import *
from core.models import *
from investors.models import *
from loans.models import *
# Create your views here.
# class GroupList(ListView):
# 	model=Category
# 	template_name='adashi/list.html'

def adashi_admin(request):
	users=User.objects.all()
	groups=AdashiGroup.objects.all()
	investors=Investment.objects.all()
	loans=Loan.objects.all()
	context={
	'users':users,
	'groups':groups,
	'investors':investors,
	'loans':loans
	}
	return render(request, 'adashi/admin/index.html',context)


def GroupList(request):
	categories=Category.objects.all()
	return render(request, 'adashi/adashi.html', {'categories':categories})


class GroupDetail(DetailView):
	model=Category
	template_name='adashi/detail.html'

class GroupUpdate(UpdateView):
	model=Category
	form_class = JoinForm
	template_name='adashi/update.html'

def join(request):
	return render(request, 'adashi/spin.html')

class JoinView(LoginRequiredMixin, CreateView):
    template_name = 'adashi/join_group.html'
    form_class = JoinForm
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
    	form.instance.user = self.request.user
    	return super().form_valid(form)


class PayView(LoginRequiredMixin, CreateView):
    template_name = 'adashi/pay.html'
    form_class = PaymentForm
    success_url = reverse_lazy('thanks')

    # def form_valid(self, form):
    # 	form.instance.user = self.request.user
    # 	return super().form_valid(form)

class CreateGroup(CreateView):
	model=AdashiGroup
	form_class=CreateGroupForm
	template_name='core/create_group.html'
	success_url=reverse_lazy('adashi-admin')
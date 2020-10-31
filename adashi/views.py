from django.conf import settings
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
from django.conf import settings
from accounts.decorators import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from rest_framework.views import APIView
from  rest_framework.response import Response
from django.views.generic import View
# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adashi/admin/admin_view.html',)

class ChartData(APIView):
    users=User.objects.all().count()
    admins=User.objects.all().filter(is_staff=True).count()
    groups=AdashiGroup.objects.all().count()
    investors=User.objects.all().filter(is_investor=True).count()
    loans=Loan.objects.all().count()
    shops=OrderItem.objects.all().count()

    def get(self, request, format=None):
        labels = ["Users",'Staff',"Adashi-Groups", "Investors", "Loans", 'Shop Loans']
        default_items = [self.users, self.admins, self.groups, self.investors,self.loans,self.shops]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

@admin_required
def adashi_admin(request):
    users = User.objects.all()
    groups = AdashiGroup.objects.all()
    investors = Investment.objects.all()
    loans = Loan.objects.all()
    context = {
        'users': users,
        'groups': groups,
        'investors': investors,
        'loans': loans
    }
    return render(request, 'adashi/admin/index.html', context)

@login_required
def GroupList(request):
    categories = AdashiGroup.objects.all()
    return render(request, 'adashi/adashi.html', {'categories': categories})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.FLUTTERWAVE_PUBLIC_KEY
        return context

class GroupDetail(LoginRequiredMixin,DetailView):
    model = AdashiGroup
    template_name = 'adashi/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.FLUTTERWAVE_PUBLIC_KEY
        return context

@method_decorator([login_required, admin_required], name='dispatch')
class GroupUpdate(UpdateView):
    model = AdashiGroup
    form_class = JoinForm
    template_name = 'adashi/update.html'

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

@method_decorator([login_required, admin_required], name='dispatch')
class CreateGroup(CreateView):
    model = AdashiGroup
    form_class = CreateGroupForm
    template_name = 'core/create_group.html'
    success_url = reverse_lazy('adashi-admin')

@admin_required
def JoinList(request):
    x = Join.objects.all().filter(approved=True)
    y = Join.objects.all().filter(approved=False)
    context = {
        'x': x,

        'y': y
    }
    return render(request, 'adashi/join_list.html', context)

@method_decorator([login_required, admin_required], name='dispatch')
class JoinUpdate(UpdateView):
    model = Join
    form_class = JoinUpdateForm
    template_name = 'adashi/update_join.html'
    success_url = reverse_lazy("join-list")

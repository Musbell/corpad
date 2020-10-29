from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView 
from django.http import HttpResponseRedirect 
from accounts.models import User 
from accounts.decorators import *
from  .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator([login_required, investor_required], name='dispatch')
class InvestmentCreate(SuccessMessageMixin , CreateView):
    model = Investment
    fields =['product','product_2','product_3','product_4','product_5','amount_invested'] 
    template_name ='investors/create_investment.html'
    success_message = "Investment Added!" 
    success_url = reverse_lazy('investment_list')
       
    def form_valid(self, form):   #the current logged in user will automatically be added as  the user 
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator([login_required, investor_required], name='dispatch')
class InvestmentList(ListView):
	model =Investment
	template_name ='investors/investment_list.html'
	
	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		context.update({
            'payments': Payment.objects.all(),})
		return context

	def get_queryset(self): #investor will only see his investments not anyone else's 
		queryset =Investment.objects.all()
		user =self.request.user
		
		if not user.is_superuser:
			queryset = queryset.filter(
			    user=self.request.user 
			)
		return queryset 

class SchemaList(LoginRequiredMixin,ListView):
	model =Schema
	template_name ='investors/schema_list.html'

@method_decorator([login_required, admin_required], name='dispatch')
class CreateSchema(CreateView):
	model=Schema
	form_class=CreateSchemaForm
	template_name='investors/create_schema.html'
	success_url=reverse_lazy('adashi-admin')




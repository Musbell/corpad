from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView 
from django.http import HttpResponseRedirect 
from accounts.models import User 
from accounts.decorators import *
from  .models import *
# from django_xhtml2pdf.views import PdfMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# @investor_required
# def InvestmentList(request):
# 	investments=Investment.objects.all()
# 	return render(request, 'investors/investment_list.html', {'investments':investments})

# 	def get_queryset(self): #investor will only see his investments not anyone else's 
# 		queryset =Investment.objects.all()
# 		user =self.request.user
		
# 		if not user.is_superuser:
# 			queryset = queryset.filter(
# 			    user=self.request.user 
# 			)
# 		return queryset 

# @investor_required
# def InvestmentCreate(request):
#     if request.method == "POST":
#         form = InvestmentForm(request.POST)
#         if form.is_valid():
#             new_investment = form.save()
#             # login(request, new_user)
#             # messages.success(request, f"you're welcome to ")
#             return redirect('investment_list')
#     else:
#         form = InvestmentForm()
#     return render(request, 'investors/create_investment.html', {'form':form})


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


class SchemaList(ListView):
	model =Schema
	template_name ='investors/schema_list.html'

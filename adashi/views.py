from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.views.generic.edit import *
from .forms import *
# Create your views here.
# class GroupList(ListView):
# 	model=Category
# 	template_name='adashi/list.html'
def GroupList(request):
	categories=Category.objects.all()
	return render(request, 'adashi/examples/dashboard.html', {'categories':categories})


class GroupDetail(DetailView):
	model=Category
	template_name='adashi/examples/detail.html'

class GroupUpdate(UpdateView):
	model=Category
	form_class = JoinForm
	template_name='adashi/update.html'

def join(request):
	return render(request, 'adashi/spin.html')

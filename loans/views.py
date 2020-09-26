from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .forms import *
from django.urls import reverse_lazy
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin


def LoanList(request):
	x=Loan.objects.all().filter(approved=True)
	y=Loan.objects.all().filter(approved=False)
	context={
	'x':x,
	'y':y
	}
	return render(request, 'loans/loan_list.html', context)
	
class LoanUpdate(LoginRequiredMixin,UpdateView):
	model = Loan
	form_class = LoanUpdateForm
	template_name='loans/update_loan.html'
	success_url = reverse_lazy("loan-list")

class LoanCreate(LoginRequiredMixin,CreateView):
	model = Loan
	form_class = LoanForm
	template_name='registration/new_loan.html'
	success_url = reverse_lazy("submitted")

	def form_valid(self, form):
		form.instance.customer = self.request.user
		return super().form_valid(form)


def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'loans/list.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'loans/cart.html', context)


def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'loans/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		# zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)


def thanks(request):
	return render(request, 'loans/thanks.html')


class CreateProduct(CreateView):
	model=Product
	form_class=CreateProductForm
	template_name='loans/create_product.html'
	success_url=reverse_lazy('adashi-admin')
from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('request-loan', views.LoanCreate.as_view(), name="request-loan"),
	# path('<int:id>/<slug:slug>/', views.commodity_detail, name='commodity_detail'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('loan-request-submitted/', views.thanks, name="submitted"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('create/commodity', views.CreateProduct.as_view(), name="create-product"),
	path('view/applications', views.LoanList, name="loan-list"),
	path('<int:pk>/approve', views.LoanUpdate.as_view(), name="loan-update"),
	path('view/shop/applications', views.ShopLoanList, name="shop-loan-list"),
	path('shop-loan/<int:pk>/approve', views.ShopLoanUpdate.as_view(), name="shop-loan-update"),

]
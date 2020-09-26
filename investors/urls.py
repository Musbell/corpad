from django.urls import path
from . import views

urlpatterns =[
         # path('create/investment', views.InvestmentCreate.as_view(),name ='create_investment'),
         path('investment/list', views.InvestmentList.as_view(),name ='investment_list'),
         path('investment/catalog', views.SchemaList.as_view(),name ='schema'),
         path('add/investment/options', views.CreateSchema.as_view(),name ='create-schema'),
] 
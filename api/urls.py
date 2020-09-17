from django.urls import path
from api import views

urlpatterns = [
    path('joins/', views.JoinList.as_view()),
    path('groups/', views.CategoryList.as_view()),
    path('join/<int:pk>/', views.JoinDetail.as_view()),
]
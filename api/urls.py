from django.urls import path
from api import views

urlpatterns = [
    path('joins/', views.JoinList.as_view()),
    path('join/<int:pk>/', views.JoinDetail.as_view()),
    path('positions/', views.PositionList.as_view()),
    path('position/<int:pk>/', views.PositionDetail.as_view()),
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('adashi/groups',views.GroupList, name="adashi"),
    path('<int:pk>/join/', views.GroupUpdate.as_view(), name="join"),
    path('group/<int:pk>/members/', views.GroupDetail.as_view(), name="detail"),
    path('join', views.join, name='join'),
    path('join/group', views.JoinView.as_view(), name='join-group'),
    path('admin', views.adashi_admin, name='adashi-admin'),
]
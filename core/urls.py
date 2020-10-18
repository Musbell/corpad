from django.urls import path 
from . import views
from  . views import *
urlpatterns = [
    path('', HomePageView.as_view(), name ='home'), 
    path("account/status/", views.index, name = "account_status"),
    path ("money/transfer/", views.money_transfer, name = "money_transfer"),
    path ("loan_app/", views.loan, name = "loan_app"),
    path('new/announcement', views.CreateAnnouncement.as_view(), name="create-announcement"),
    path('new/notification', views.CreateNotification.as_view(), name="create-notification"),
    path('announcements', views.announcements, name="announcements"),
    path('notifications', views.notifications, name="notifications"),
     path('add/money', views.addMoney, name="add-money"),
     path('withdraw/money', views.withdraw, name="withdraw"),
]
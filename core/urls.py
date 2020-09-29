from django.urls import path 
from . import views
from  . views import *
urlpatterns = [
    path('', HomePageView.as_view(), name ='home'), 
    path("account/status/", views.index, name = "account_status"),
    path ("money/transfer/", views.money_transfer, name = "money_transfer"),
    path ("loan_app/", views.loan, name = "loan_app"),
    path('new/announcement', views.Announcement.as_view(), name="create-announcement"),
     path('new/notification', views.Notification.as_view(), name="create-notification")
]
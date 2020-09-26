from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name="register"),
    path('profiles/', ProfileList.as_view(), name="profile_list"),
    path('<int:pk>/', ProfileDetail.as_view(), name="profile_detail"),
    path('login/', LoginView.as_view(
        template_name="registration/login.html"),
        name="login"
    ),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', profile, name="profile"),
    path('profile/update/', profileUpdate, name="profile_update"),
    # path('profile/update/', ProfileUpdate, name="update"),
    path('verify/', Verify.as_view(), name="verify"),
    path('message/', Message.as_view(), name="message"),
    path('messages/', MessageList.as_view(), name="message-list"),
    path('message-sent/', message_sent, name="message-sent"),
    path('thanks/', thanks, name="thanks"),
    path('user/dashboard', user_dashboard, name="user-dashboard"),
    path('all/users', list_users, name="users_list"),
    path('all/investors', list_investors, name="investors_list"),
   
]
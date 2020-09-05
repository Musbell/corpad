from django.urls import path
from .views import register,profile, profileUpdate, ProfileList, ProfileDetail, Verify, thanks
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
    path('thanks/', thanks, name="thanks")
]
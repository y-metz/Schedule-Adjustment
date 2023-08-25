from django.urls import path
from .views import SignupView, UserLoginView, UserProfileView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
]

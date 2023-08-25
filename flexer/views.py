from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .models import UserEventTimeSlot

# ユーザー登録
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user_login')

# ログイン
class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


# ユーザー情報の表示
class UserProfileView(ListView):
    template_name = 'profile.html'
    context_object_name = 'events'

    def get_queryset(self):
        return UserEventTimeSlot.objects.filter(user=self.request.user)

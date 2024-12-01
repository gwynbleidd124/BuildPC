from django.contrib.auth import logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from Build.models import Computer
from users.forms import LoginUserForm, RegisterUserForm, ProfileForm, UserChangePasswordForm

app_name = 'users'

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('homepage'))

class ProfileUsers(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['computer'] = self.request.user.author.all()
        return context

class ChangePassword(PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_change_done')

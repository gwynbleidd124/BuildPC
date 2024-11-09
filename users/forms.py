from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    captcha = CaptchaField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', )
        labels = {
            'username': 'Никнейм',
            'email': 'E-Mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль',
            'password2': 'Повторите пароль',
        }

    def clean_password(self):
            cd = self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError('Пароли не совпадают!')
            return cd['password1']

    def clean_email(self):
            email = self.cleaned_data['email']
            if get_user_model().objects .filter(email=email).exists():
                raise forms.ValidationError('Пользователь с таким Email адресом уже существует')
            return email


class ProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'email': 'E-Mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class UserChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
  username      = forms.CharField(label='Kullanıcı Adınız',widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı Adınız'}))
  email         = forms.EmailField(label='E-mail Adresiniz',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  #email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
  first_name    = forms.CharField(label='Adınız',widget=forms.TextInput(attrs={'placeholder': 'Adınız'}))
  last_name     = forms.CharField(label='Soyadınız',widget=forms.TextInput(attrs={'placeholder': 'Soyadınız'}))
  password1     = forms.CharField(label='Parolanız',widget=forms.PasswordInput(attrs={'placeholder': 'Parolanız'}))
  password2     = forms.CharField(label='Parola Doğrulama',widget=forms.PasswordInput(attrs={'placeholder': 'Parolanızı Tekrar Girin'}))

  class Meta:
      model = User
      fields = ['username', 'email', 'first_name', 'last_name','password1','password2']

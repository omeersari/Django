from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class NewUserForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı Adı giriniz', min_length=4, max_length=150)
    email = forms.EmailField(label='Email adresinizi giriniz')
    password1 = forms.CharField(label='Şifrenizi giriniz', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Şifrenizi doğrulayınız', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Kullanıcı Adı Zaten Mevcut")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email Adresi Zaten Mevcut")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class EditUserNameForm(UserChangeForm):
    username = forms.CharField(label='Kullanıcı Adı Giriniz', min_length=4, max_length=150)
    email = None
    password = None

    class Meta:
        model = User
        fields = ("username",)

class EditEmailForm(UserChangeForm):
    username = None
    email = forms.CharField(label='Email Adresini Giriniz', min_length=4, max_length=150)
    password = None

    class Meta:
        model = User
        fields = ("email",)




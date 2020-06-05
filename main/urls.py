"""realsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name="main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register/", views.register, name="register"),
    #path("activated/", views.activate_account, name="activate"),
    path("register/form/", views.form, name="form"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("account/", views.account_view, name="account_view"),
    path("edit/", views.edit_account, name="edit_account"),
    path("editUsername/", views.edit_Username, name="edit_username"),
    path("editEmail/", views.edit_Email, name="edit_email"),
    path("duyurular/", views.duyurular, name="duyurular"),
    path("premium/", views.premium, name="premium"),
    path("get_premium/", views.get_premium, name="get_premium"),
    path("iletisim/", views.iletisim, name="iletisim"),
    path("yardim/", views.yardim, name="yardim"),
    

    
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name = "main/accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name = "main/accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name = "main/accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name = "main/accounts/password_reset_complete.html"), name="password_reset_complete"),

    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="main/accounts/password_change.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name = "main/accounts/password_change_done.html"), name= "password_change_done"),
    
] 



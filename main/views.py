from django.shortcuts import render, redirect, get_object_or_404, reverse, Http404
from django.http import HttpResponse
from .models import Author, Duyuru, UserProfile
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import logout, authenticate, login
from .forms import NewUserForm, EditUserNameForm, EditEmailForm
from .helpers import generate_activation_key
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users


# Create your views here.

def homepage(request):
    """duyurular = [d.duyurular_published for d in Duyurular.objects.all()]
    uzunluk = len(duyurular)
    user = request.user
    
    
    if user.is_authenticated:
        a = UserProfile.objects.filter(user=user).last()
        i = 0
        u = User.objects.get(username=user.username)
        last_login = u.user.login_last
        for datetime in duyurular:
            if last_login <= datetime:
                i = i + 1
    """
    return render(request = request,
                 template_name='main/homepage.html')
    



@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
                user= form.save()
                #group = Group.objects.get(name="Standart")
                #user.groups.add(group)
                return redirect("main:form")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request,
                      'main/register.html',
                      {"form":form})

    form = NewUserForm
    return render(request,
                  'main/register.html',
                  {"form":form})

def form(request):
    return render(request,
                  'main/form.html')

def logout_request(request):
    logout(request)
    messages.info(request, "Başarıyla çıkış yaptınız")
    return redirect("main:homepage")

@unauthenticated_user
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"{username} ile giriş yaptınız!")
                return redirect('/')
            else:
                messages.error(request, "Kullanıcı adı veya şifre hatalı")
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı")


    form = AuthenticationForm()
    return render(request,
                "main/login.html",
                {"form":form})

def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()
 
    r = get_object_or_404(Author, activation_key=key, email_validated=False)
    r.user.is_active = True
    r.user.save()
    r.email_validated = True
    r.save()
 
    return render(request, 'main/activated.html')


def account_view(request):
    account = request.user
    #group = request.user.groups.filter(name="Standart").values_list("name", flat=True)
    #group_list = list(group)
    #group0 = group_list[0]
    return render(request,
                   "main/account.html",
                   {"account":account,
                   #"groupname":group0
                   })

def edit_account(request):
    user = request.user
    return render(request,
                 "main/accounts/edit.html",
                 {"user":user})

def edit_Username(request):
    if request.method == "POST":
        form = EditUserNameForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Kullanıcı adınızı başarıyla değiştirdiniz !")
            return redirect("main:account_view")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
            
    
    form = EditUserNameForm(instance=request.user)
    return render(request,
                "main/accounts/editUsername.html",
                {"form":form})


def edit_Email(request):
    if request.method == "POST":
        form = EditEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Email adresinizi başarıyla değiştirdiniz !")
            return redirect("main:account_view")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    
    form = EditEmailForm(instance=request.user)
    return render(request,
                 "main/accounts/editEmail.html",
                 {"form":form})

#@allowed_users(allowed_roles = ['Premium'])
def duyurular(request):
    return render(request,
                  "main/duyurular.html",
                  {"duyurular":Duyuru.objects.all})


def premium(request):
    return render(request,
                  "main/premium.html"
                  )


def get_premium(request):
    return render(request,
                "premium/get_premium.html")


def iletisim(request):
    return render(request,
                 "main/iletisim.html")





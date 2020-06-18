from django.contrib import admin
from .models import Author, Duyuru
from tinymce.widgets import TinyMCE
from django.db import models
from django.contrib.auth.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = [
        "USERNAME"
        "EMAIL ADDRESS"
        "Groups"
        "STAFF STATUS"
    ]


admin.site.register(Duyuru)







from dataclasses import fields
from random import choices
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
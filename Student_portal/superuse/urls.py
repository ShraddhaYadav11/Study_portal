from django.urls import URLPattern, path
from . import views
from superuse import views as super_views
from django.contrib.auth import views as auth_views

urlpatterns=[
     path('',views.home,name="home"),
]

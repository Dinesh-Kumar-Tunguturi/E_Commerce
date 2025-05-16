from django.urls import path
from .views.home import home
from .views.signup import signup
from .views.login import login



urlpatterns = [
    path("", home.as_view()),
    path("signup", signup.as_view(),name='signup'),
    path('login',login.as_view(), name='login')
]
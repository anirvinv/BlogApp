from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.log_in, name="log_in"),
    path('logout', views.log_out, name="log_out"),
    path('signup', views.sign_up, name="sign_up"),
    path('user', views.user_info, name="user_info")
    ]
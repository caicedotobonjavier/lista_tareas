from django.urls import path

app_name = 'users_app'

from . import views

urlpatterns = [
    path('new-user', views.NewUserView.as_view(), name='new_user'),
    path('login-user', views.LoginUserView.as_view(), name='login_user'),
    path('logout-user', views.LogoutView.as_view(), name='logout_user'),
]

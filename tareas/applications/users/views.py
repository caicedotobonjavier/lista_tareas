from django.shortcuts import render
#
from .models import User
#
from django.views.generic import FormView, View
#
from .forms import UserForm, LoginForm
#
from django.urls import reverse_lazy, reverse
#
from django.http import HttpResponseRedirect
#
from django.contrib.auth import login, authenticate, logout
#

class NewUserView(FormView):
    template_name = 'users/new_user.html'
    form_class = UserForm
    success_url = '.'

    def form_valid(self, form):
        
        direccion = form.cleaned_data['address']
        date = form.cleaned_data['date_birth']
        telefono = form.cleaned_data['phone']
        foto = form.cleaned_data['photo']

        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['full_name'],
            form.cleaned_data['password'],
            address = direccion,
            date_birth = date,
            phone = telefono,
            photo = foto
        )

        return HttpResponseRedirect(
            reverse(
                'users_app:new_user'
            )
        )



class LoginUserView(FormView):
    template_name = 'users/login_user.html'
    form_class = LoginForm
    success_url = '.'


    def form_valid(self, form):
        usuario = form.cleaned_data['email']
        contrasena = form.cleaned_data['password']

        login_user = authenticate(email=usuario, password=contrasena)

        login(self.request, login_user)

        return HttpResponseRedirect(
            reverse(
                'home_app:index'
            )
        )



class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'users_app:login_user'
            )
        )
    
from django.urls import path

app_name = 'home_app'

from . import views

urlpatterns = [
    path('index', views.IndexView.as_view(), name='index'),
]

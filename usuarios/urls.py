from django.urls import path, include
from . import views

app_name = "usuarios"
urlpatterns = [
    path('', views.registrarse, name="registrarse"),
]
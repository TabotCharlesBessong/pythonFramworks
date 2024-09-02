from django.urls import path
from . import views

# define a list of urls patterns
urlpatterns = [
    path("",views.index)
]

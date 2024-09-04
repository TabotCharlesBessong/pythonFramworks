from django.urls import path
from . import views

# define a list of urls patterns
urlpatterns = [
    path("",views.index,name='home'),
    path("contact/",views.contact_view,name="contact"),
    path("contact/success",views.contact_success_view,name="contact-success"),
]

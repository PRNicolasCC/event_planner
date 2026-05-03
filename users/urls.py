from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro
from .forms import OrganizadorLoginForm

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        authentication_form=OrganizadorLoginForm
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
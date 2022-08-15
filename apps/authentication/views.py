from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView

from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from apps.users.decorators import unauthenticated_user

from apps.users.forms import MyUserCreationForm,LoginForm
from apps.users.models import CustomUser

# Create your views here.

class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy("authentication:login")
    template_name = "authentication/register.html"


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if request.method == "POST":

            if form.is_valid():
                email = form.cleaned_data.get("email")
                password = form.cleaned_data.get("password")
                user = authenticate(email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.info(request, "Invalid User")
            else:
                 messages.info(request, "Invalid Info")

    else:
         form = LoginForm()
    context = {
            'form':form
        }
    return render(request, 'authentication/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("/accounts/login")
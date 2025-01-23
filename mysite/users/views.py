from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from users.forms import RegistrationForm
from django.contrib.auth.models import User
def login_user(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["login"], password=request.POST["password"])
        if user is not None:
            """
            Сохраняет идентификатор пользователя в сессии, используя фреймворк сессий Django
            """
            login(request=request, user=user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, template_name="users/login.html", context={"error_message": "Invalid credentials"})
    else:
        return render(request=request, template_name="users/login.html")

def registration_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            login = form.cleaned_data["login"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=login, email=email, password=password)
            user.save()
            return HttpResponseRedirect(reverse("users:login"))
    else:
        form = RegistrationForm()
    return render(request=request, template_name="users/registration.html", context={"form": form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("view_students")

    def get_success_url(self):
        return reverse_lazy("view_students")

def user_logout(request):
    logout(request)
    return redirect("login")
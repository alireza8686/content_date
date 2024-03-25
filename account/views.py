from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('panel',user.id)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel', user_id=user.id)
            else:
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    return redirect("home")
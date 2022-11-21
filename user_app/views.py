from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


# Create your views here.

def login_user(request):
    if request.method == 'POST': # user post smth on page
        username = request.POST['username'] # take it from the form login.html
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
                # Redirect to a success page.
            return redirect('main')
        else:
                # Return an 'invalid login' error message.
            messages.success(request, ('There was a login error. Try again'))
            return redirect('login_user')  # if smth goes wrong with login - then 'login' page again
    else:
        return render(request, 'authenticate/login.html', {})   # show page to user on site

def logout_user(request):
    logout(request)
    messages.success(request, ('You were log-out. Remember to leave some review ! See You Later - YOUR NAME HERE' ))
    return redirect('main')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration successful!'))
            return redirect('main')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form,})
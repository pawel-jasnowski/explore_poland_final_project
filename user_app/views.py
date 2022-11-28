from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterUserForm, PasswordChangingForm, EditProfileForm



def login_user(request):
    if request.method == 'POST': # user post smth on page
        username = request.POST['username'] # take it from the form login.html
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
                # Redirect to a success page.
            return render(request, 'home_for_user.html', {})
            # return redirect('main') # NOT WORKINH THIS WAY  ???
        else:
                # Return an 'invalid login' error message.
            messages.success(request, ('There was a login error. Try again'))
            return redirect('login_user')  # if smth goes wrong with login - then 'login' page again
    else:
        return render(request, 'authenticate/login.html', {})   # show page to user on site

def logout_user(request):

    logout(request)
    messages.success(request, f'You were log-out. See You later!')
    return render(request, 'home_for_user.html', {})

    # return redirect('main')  NOT WORKING HIS WAY ???

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
            return render(request, 'home_for_user.html', {})
            # return redirect('main') # NOT WORKING tHIS WAY
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form,})

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home_page_app:main')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('home_page_app:main')

    def get_object(self):
        return self.request.user


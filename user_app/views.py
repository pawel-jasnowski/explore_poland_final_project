from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView

from django.urls import reverse_lazy
from django.views import generic

#################### email confirmation
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .forms import RegisterUserForm, PasswordChangingForm, EditProfileForm
from .tokens import account_activation_token



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
            messages.success(request, f'There was a login error. Try again')
            return redirect('login_user')  # if smth goes wrong with login - then 'login' page again
    else:
        return render(request, 'authenticate/login.html', {})   # show page to user on site

def logout_user(request):
    logout(request)
    messages.success(request, ('You were log-out. Remember to leave some review ! See You Later - YOUR NAME HERE' ))
    return redirect('main')

##################### email activation #####################

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode((uidb64)))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, f"Thank You for your email confirmation. {user.username} - You can login now to your account")
        return redirect('login_user')
    else:
        messages.erros(request, "Activation link is invalid!")

    return redirect('main')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account'
    message = render_to_string("authenticate/template_activate_account.html", {

        'user':user.username,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)), #primary key converet to string
        'token':account_activation_token.make_token(user),
        "Protocol":'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user.username} go to Your email: {to_email}, and please confirm your registration')
    else:
        messages.error(request,f'There was some probem sending email')
#################################
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            #################### email changing :
            # form.save()
            user = form.save(commit=False)
            user.is_activate = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))

            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # email = form.cleaned_data['email']
            # user = authenticate(username=username, password=password, email=email)
            # login(request, user)
            messages.success(request, f'New account created for {user.username}')   #doesnt work .... !
            return redirect('login_user')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form':form,})

class PasswordsChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('main')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authenticate/edit_profile.html'
    success_url = reverse_lazy('main')

    def get_object(self):
        return self.request.user


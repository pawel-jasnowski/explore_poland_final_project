from django.urls import path, include, reverse_lazy
from .import views
from .views import PasswordsChangeView, UserEditView

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('password_change', PasswordsChangeView.as_view(template_name='authenticate/change_password.html'), name='password_change'),
    path('profile_edit', UserEditView.as_view(), name='profile_edit'),

    ]
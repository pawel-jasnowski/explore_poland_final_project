def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            #################### email changing
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            # messages.success(request, 'Registration successful!')   #doesnt work .... !
            return redirect('main')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html', {'form': form, })
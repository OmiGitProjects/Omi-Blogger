# TODO: Handling User Authentication, Verifying, PasswordReset
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Register Form
def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} Your Account is Created!')        
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'users_/register.html', context)

#Login Form
#FIXME:
def login_(request):
    #Request POST
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        # User Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, f'Type Correct Credentials!!!')
            return redirect('homepage')

    context = {}
    return render(request, 'users_/login.html', context)

# Logout URL
def logout_(request):
    logout(request)
    return redirect('homepage')
from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomRegistrationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ('New user account created, login to get started!'))
            return redirect('register')
    else:
        register_form = CustomRegistrationForm()
    
    return render(request, 'register.html', {'register_form': register_form})
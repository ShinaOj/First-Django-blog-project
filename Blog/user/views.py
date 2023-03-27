from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def register_view(request):
    form=UserRegistrationForm()
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created succesfully")
            return redirect("home")
    context={
        'form':form
    }
    return render(request, 'user/register.html', context)

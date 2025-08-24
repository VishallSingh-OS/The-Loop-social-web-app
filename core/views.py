from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages

# Create your views here


def home(request):
    return render(request, 'core/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please Log In.')
            return redirect('login')
        
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form}) # form is context dictionary so we can use this in html template
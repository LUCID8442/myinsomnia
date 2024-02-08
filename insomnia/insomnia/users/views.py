from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = SignUpForm()
    return render(request, 'insomnia\users\templates\sign_up.html', {'form': form})

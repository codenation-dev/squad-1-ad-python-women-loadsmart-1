from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.forms import SignUpForm


# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/events')
    else:    
        form= UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

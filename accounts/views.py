from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User

from django_email_verification import send_email

from .forms import UserRegistrationForm

def registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data['email']
            user_username = form.cleaned_data['username']
            user_password = form.cleaned_data['password1']

            user = User.objects.create(
                username=user_username,
                email=user_email
            )
            user.set_password(user_password)
            user.is_active = False
            send_email(user)
            
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'registration/registration.html', {'form':form})
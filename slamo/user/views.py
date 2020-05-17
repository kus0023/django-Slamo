from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        return render(request, 'user/signin.html')
    else:
        return render(request, 'user/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main')
        else:
            message = 'Username and password are incorrect'
            return render(request, 'user/signin.html', context={'message': message})
    else:
        return render(request, 'user/signin.html')

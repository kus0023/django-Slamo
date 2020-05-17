from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def main(request):
    if request.user.is_authenticated:
        return render(request, 'main/home.html')
    return HttpResponseRedirect('user')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin')


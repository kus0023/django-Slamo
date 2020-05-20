from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def main(request):
    if request.user.is_authenticated:
        return render(request, 'main/home.html')
    return HttpResponseRedirect('/')


def sendSlam(request):
    return render(request, 'main/send-slam.html')

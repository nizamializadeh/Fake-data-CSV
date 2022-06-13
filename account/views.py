from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/schemas')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/schemas')
        else:
            return redirect('acconuts')

    return render(request, "login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

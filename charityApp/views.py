from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def start(request):
    return redirect('/login')


def signup_view(request):
    # POST request - when user tries to sign up
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # sign up user if info is valid
        if form.is_valid():
            # login user
            user = form.save()
            login(request, user)
            return redirect('/explore')
    # GET request - when user accesses page
    else:
        form = UserCreationForm()
    # render sign up form
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    # POST request - when user tries to log in
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        # sign up user if info is valid
        if form.is_valid():
            # login user
            user = form.get_user()
            login(request, user)

            # If 'next' exists, redirect users back to page (before prompted for login)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/explore')
    # GET request - when user accesses page
    else:
        form = AuthenticationForm()
    # render login form
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    # POST request - when user tries to log out
    if request.method == 'POST':
        # logout user
        logout(request)
        return render(request, 'logout.html')


@login_required(login_url="/login")
def explore(request):
    return render(request, 'explore.html')

@login_required(login_url="/login")
def account(request):
    return render(request, 'account.html')

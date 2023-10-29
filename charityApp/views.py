from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.db.models import Count
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from .models import Charity
from .models import Community
from .models import User_History
from .models import User_Community
from .models import Community_History
from .models import Community_Charity
from .models import Community_Comment
from django.contrib.auth.models import User


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
    communities = Community.objects.all()
    communityUserCount = User_Community.objects.values('communityID').annotate(count=Count('communityID'))
    charities = Charity.objects.all()


    #cotm = Community.objects.get(id=1)
    #print(cotm.community_charity_set.all())


    return render(request, 'explore.html', {'communities': communities, 'communityUserCount': communityUserCount, 'charities': charities})

@login_required(login_url="/login")
def account(request):
    user = request.user
    # userCommunityCount = User_Community.objects.values('username').annotate(count=Count('username'))
    # print(userCommunityCount)
    userCommunities = User_Community.objects.filter(username=user)
    userHistories = User_History.objects.filter(username=user)
    return render(request, 'account.html', {'user': user, 'userCommunities': userCommunities, 'userHistories': userHistories})

@login_required(login_url="/login")
def animals(request):
    return render(request, 'communities/animals.html')

@login_required(login_url="/login")
def arts_culture(request):
    return render(request, 'communities/arts&culture.html')

@login_required(login_url="/login")
def education(request):
    return render(request, 'communities/education.html')

@login_required(login_url="/login")
def environment(request):
    return render(request, 'communities/environment.html')

@login_required(login_url="/login")
def health(request):
    return render(request, 'communities/health.html')

@login_required(login_url="/login")
def indigenouspeoples(request):
    return render(request, 'communities/indigenouspeoples.html')

@login_required(login_url="/login")
def publicbenefit(request):
    return render(request, 'communities/publicbenefit.html')

@login_required(login_url="/login")
def socialservices(request):
    return render(request, 'communities/socialservices.html')

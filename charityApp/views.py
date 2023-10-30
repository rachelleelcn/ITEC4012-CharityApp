from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import admin
from .models import Charity
from .models import Community
from .models import User_History
from .models import User_Community
from .models import Community_History
from .models import Community_Charity
from .models import Community_Comment
from django.contrib.auth.models import User
from .forms import CommentForm



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

@require_POST
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


@login_required(login_url="/login")
def explore(request):
    communities = Community.objects.all()
    communityUserCount = User_Community.objects.values('communityID').annotate(count=Count('communityID'))
    charities = Charity.objects.all()

    return render(request, 'explore.html', {'communities': communities, 'communityUserCount': communityUserCount, 'charities': charities})

@login_required(login_url="/login")
def account(request):
    user = request.user
    userCommunities = User_Community.objects.filter(username=user)
    userHistories = User_History.objects.filter(username=user)
    return render(request, 'account.html', {'user': user, 'userCommunities': userCommunities, 'userHistories': userHistories})

@require_POST
def communitycomment(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.username = request.user
        instance.communityID = Community.objects.get(name=request.POST.get('prevCommunity'))
        instance.save()
        return redirect(request.POST.get('prevPath'))

@require_POST
def joincommunity(request):
    user = request.user
    community = Community.objects.get(name=request.POST.get('prevCommunity'))
    if request.POST.get("status") == 'Join':
        # user_community add row
        User_Community(username=user, communityID=community).save()
    else:
        # delete row
        User_Community.objects.get(username=user, communityID=community).delete()
    return redirect(request.POST.get('prevPath'))


@login_required(login_url="/login")
def animals(request):
    community = Community.objects.get(id=1)
    userCount = community.user_community_set.all().count()
    lastHistory = community.community_history_set.all().last()
    charities = community.community_charity_set.all()
    comments = community.community_comment_set.all()
    user = request.user
    userCommunities = User_Community.objects.filter(username=user)

    # Check if user joined the community
    join = False
    for item in userCommunities:
        if str(item.communityID) == str(community.name):
            join = True

    # Fetch form from forms
    commentform = CommentForm()

    return render(request, 'communities/animals.html',
                  {'community': community, 'userCount': userCount, 'lastHistory': lastHistory, 'charities': charities,
                   'comments': comments, 'commentform': commentform, 'userCommunities': userCommunities, 'join': join})

@login_required(login_url="/login")
def arts_culture(request):
    pass


@login_required(login_url="/login")
def education(request):
    pass

@login_required(login_url="/login")
def environment(request):
    pass

@login_required(login_url="/login")
def health(request):
    pass

@login_required(login_url="/login")
def indigenouspeoples(request):
    pass

@login_required(login_url="/login")
def publicbenefit(request):
    pass

@login_required(login_url="/login")
def socialservices(request):
    pass




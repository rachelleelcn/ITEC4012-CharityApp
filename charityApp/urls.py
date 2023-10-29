from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('explore/', views.explore, name='explore'),
    path('account/', views.account, name='account'),
    path('explore/animals/', views.animals, name='animals'),
    path('explore/arts&culture/', views.arts_culture, name='arts&culture'),
    path('explore/education/', views.education, name='education'),
    path('explore/environment/', views.environment, name='environment'),
    path('explore/health/', views.health, name='health'),
    path('explore/indigenouspeoples/', views.indigenouspeoples, name='indigenouspeoples'),
    path('explore/publicbenefit/', views.publicbenefit, name='publicbenefit'),
    path('explore/socialservices/', views.socialservices, name='socialservices')
]

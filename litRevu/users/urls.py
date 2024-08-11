from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('home', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('tickets/', include('tickets.urls')),
    path('followers/', include('followers.urls')),
    path('flux/', include('flux.urls'), name='flux'),
]

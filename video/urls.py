from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index,home,profile,register,login_view,detail_profile,members
urlpatterns = [
    path('',home,name="home"),
    path('feed/',index,name="feed"),
    path('profile/',profile,name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/',register,name='register'),
    path('login/',login_view,name="login"),
    path('profile_detail/<int:id>',detail_profile,name="detail"),
    path('members/',members,name='members'),
    #path('send_friend_request/<int:receiver_id>',send_friend_request, name='send_friend_request'),
#path('accept_friend_request/<int:friend_request_id>',accept_friend_request, name='accept_friend_request'),
    
] 
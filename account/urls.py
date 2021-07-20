from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', LoginUserView.as_view()
    , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html") , name='userlogout'),
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('user/<int:pk>', UserDetailView.as_view() , name='userdetail'),
    path('user/<int:pk>/update', UserUpdateView.as_view() , name='userupdate'),
    path('user/<int:pk>/delete', UserDeleteView.as_view() , name='userdelete'),
    path('user/create', UserCreateView.as_view() , name='usercreate'),
]
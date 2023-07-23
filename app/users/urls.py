from django.urls import path

from .views import (
    CreateUserView,
    UserLoginView,
    UserLogoutView,
)

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
from django.urls import path
from .views import (
    HomeView,
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    LoginView,
    logout_user
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='get_users'),
    path('users/create/', UserCreateView.as_view(), name='create_user'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/<int:id>/', logout_user, name='logout'),
]

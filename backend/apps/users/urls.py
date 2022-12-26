from django.urls import path

from .views import GetUserView, UpdateProfileView, UserCreateView, UserListCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/list', UserListCreateView.as_view()),
    path('/update', UpdateProfileView.as_view()),
    path('/user', GetUserView.as_view()),
]

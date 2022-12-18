from django.urls import path

from .views import UpdateProfileView, UserCreateView, UserListCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/list', UserListCreateView.as_view()),
    path('/update', UpdateProfileView.as_view()),
]

from django.urls import path

from .views import UserCreateView, UserListCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/list', UserListCreateView.as_view()),
    # path('/user', UserRetrieveUpdateDestroyView.as_view()),
]
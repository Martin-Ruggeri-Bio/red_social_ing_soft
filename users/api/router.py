from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView


urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='User'),
    path('user/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='User')
]

from django.urls import path
from .views import UserProfileListCreateView, UserProfileRetrieveUpdateDestroyView


urlpatterns = [
    path('userProfile/', UserProfileListCreateView.as_view(), name='UserProfile'),
    path('userProfile/<int:id>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='UserProfile')
]

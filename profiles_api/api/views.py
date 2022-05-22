from django.db.models.query import QuerySet
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .paginations import SmallResultsSetPagination
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import UpdateOwnProfile
from rest_framework import filters as df


class UserProfileListCreateView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = UserProfile.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', 'email')
    ordering_fields = ('name', )


class UserProfileRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = UserProfile.objects.all()
    lookup_field = 'id'

from django.db.models.query import QuerySet
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .paginations import SmallResultsSetPagination
from ..models import User
from .serializers import UserSerializer
from .permissions import UpdateOwnProfile
from rest_framework import filters as df


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = User.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (df.OrderingFilter, df.SearchFilter, )
    search_fields = ('name', 'email')
    ordering_fields = ('name', )


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    queryset = User.objects.all()
    lookup_field = 'id'

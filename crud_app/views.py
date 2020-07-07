from django.shortcuts import render
from rest_framework import status, response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import userProfile
from .permission import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, userSerializer
from django.contrib.auth.models import User


# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.data
        user.profile = 1
        serializer = userProfileSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    authentication_classes = ()
    permission_classes = ()
    queryset = userProfile.objects.all()
    serializer_class = userProfileSerializer
# permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class userView(ListCreateAPIView):
    queryset = User.objects.all()

    def post(self, request):
        user = request.data
        serializer = userSerializer(data=user)
        if serializer.is_valid():
            user_save = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = userSerializer

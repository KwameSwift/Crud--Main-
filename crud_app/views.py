from django.shortcuts import render
from rest_framework import status, response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import userProfile
from .permission import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, userSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = userProfileSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = userProfile.objects.all()
        return queryset

    def post(self, request):
        user = request.data
        user.profile = 1
        email_verify = User.objects.filter(email=request.data.get('email'))
        if len(email_verify) > 0:
            return Response('Email already taken', status.HTTP_400_BAD_REQUEST)
        else:
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
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    serializer_class = userSerializer


class userLogin(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Response({"token": user.auth_token})
        else:
            Response({'error': "Wrong credentials"})

from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import UserCreateSerializer, AuthTokenSerializer, UserSerializer, StorySerializer, StorySubmitSerializer
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Story
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, parsers, renderers


class NewUser(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def post(request):
        serializer = UserCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)
            user.save()
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (parsers.JSONParser, parsers.FormParser)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        user_data = UserSerializer(user, context={'request': request}).data
        user_data['token'] = token.key
        return Response(user_data, status=status.HTTP_202_ACCEPTED)


class Logout(APIView):
    @staticmethod
    def get(request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)


class SubmitStory(APIView):

    @staticmethod
    def post(request):
        serializer = StorySubmitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            story = serializer.save()
            story.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        errors = serializer.errors
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class GetStoryList(APIView):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def get(request):
        stories = Story.objects.all()
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)



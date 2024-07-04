from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup(request):
    serializer = UserSerializer(data=json.loads(request.body))
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([AllowAny])
def protected_view(request):
    return Response({"message": "This is a protected view"})


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data = json.loads(request.body)
    
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        # return Response({
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        # })
        return Response("User Login successfully")
    return Response({"detail": "Invalid credentials"}, status=400)


from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import Users
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status


class UsersAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            users=Users.objects.all()
            users_serializers = UsersSerializer(users, many=True)
            return Response(users_serializers.data)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):        
        try:
            users_serializers = UsersSerializer(data=request.data, many=True)
            if users_serializers.is_valid():
                users_serializers.save()
                return Response(users_serializers.data, status=status.HTTP_201_CREATED) 
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Users.DoesNotExist:
            return Response(users_serializers.errors, status=status.HTTP_404_NOT_FOUND)


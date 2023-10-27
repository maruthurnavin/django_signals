from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from .models import User

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            # sent a signal to the email
            
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

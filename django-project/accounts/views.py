from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import CustomRegisterSerializer, CustomUserDetailSerializer
from .models import User



@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request, nickname):
    user = get_object_or_404(User, nickname=nickname)

    if request.method == 'GET':
        serializer = CustomRegisterSerializer(user)
        # print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        # Exclude nickname from the request data if it exists
        data = request.data.copy()
        data.pop('nickname', None)
        serializer = CustomRegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(request=request)
            return Response(serializer.data, status=status.HTTP_200_OK)


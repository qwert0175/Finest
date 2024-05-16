from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, DetailUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    
    class Meta:
        model = DetailUser
        fields = '__all__'
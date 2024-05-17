from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True, max_length=10)
    nickname = serializers.CharField(required=True, max_length=10)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'nickname', 'email', 'password1', 'password2')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = self.validated_data.get('username', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        data['email'] = self.validated_data.get('email', '')
        return data
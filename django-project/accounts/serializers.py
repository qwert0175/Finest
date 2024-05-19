from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from .models import User

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, allow_blank=False, max_length=10)
    email = serializers.EmailField(required=False, allow_blank=True)
    gender = serializers.ChoiceField(required=False, allow_blank=True, choices=User.GENDER_CHOICES)
    age = serializers.IntegerField(required=False, max_value=99)
    birthday = serializers.DateField(required=False)
    salary = serializers.IntegerField(required=False, max_value=999999999999)
    asset = serializers.IntegerField(required=False, max_value=999999999999)
    debt = serializers.IntegerField(required=False, max_value=999999999999)
    profile_image = serializers.ImageField(required=False, use_url=True)    
    # deposit = serializers.IntegerField(required=False)
    # saving = serializers.IntegerField(required=False,)
   
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', None),
            'birthday': self.validated_data.get('birthday', None),
            'salary': self.validated_data.get('salary', None),
            'asset': self.validated_data.get('asset', None),
            'debt': self.validated_data.get('debt', None),
            'profile_image': self.validated_data.get('profile_image', None),
        }

class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        # see https://github.com/iMerica/dj-rest-auth/issues/181
        # UserModel.XYZ causing attribute error while importing other
        # classes from `serializers.py`. So, we need to check whether the auth model has
        # the attribute or not
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'gender'):
            extra_fields.append('gender')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'birthday'):
            extra_fields.append('birthday')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
        if hasattr(UserModel, 'asset'):
            extra_fields.append('asset')
        if hasattr(UserModel, 'debt'):
            extra_fields.append('debt')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
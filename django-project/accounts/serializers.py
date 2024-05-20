from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from .models import User

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True, allow_blank=False, max_length=10)
    email = serializers.EmailField(required=False, allow_blank=True)
    # lastname = serializers.CharField(required=False, allow_blank=True, max_length=10)
    # firstname = serializers.CharField(required=False, allow_blank=True, max_length=10)
    gender = serializers.ChoiceField(required=False, allow_blank=True, choices=User.GENDER_CHOICES)
    age = serializers.IntegerField(required=False, max_value=99)
    birthday = serializers.DateField(required=False)
    salary = serializers.IntegerField(required=False, max_value=999999999999)
    asset = serializers.IntegerField(required=False, max_value=999999999999)
    debt = serializers.IntegerField(required=False, max_value=999999999999)
    deposit = serializers.IntegerField(required=False, max_value=999999999999)
    saving = serializers.IntegerField(required=False, max_value=999999999999)
    is_staff = serializers.BooleanField(default=False)
    profile_image = serializers.ImageField(required=False, use_url=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'lastname': self.validated_data.get('lastname', ''),
            'firstname': self.validated_data.get('firstname', ''),
            'gender': self.validated_data.get('gender', ''),
            'age': self.validated_data.get('age', None),
            'birthday': self.validated_data.get('birthday', None),
            'salary': self.validated_data.get('salary', 0),
            'asset': self.validated_data.get('asset', 0),
            'debt': self.validated_data.get('debt', 0),
            'deposit': self.validated_data.get('deposit', 0),
            'saving': self.validated_data.get('saving', 0),
            'credit_loan': self.validated_data.get('credit_loan', 0),
            'is_staff': self.validated_data.get('is_staff', False),
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
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
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
        if hasattr(UserModel, 'deposit'):
            extra_fields.append('deposit')
        if hasattr(UserModel, 'saving'):
            extra_fields.append('saving')
        if hasattr(UserModel, 'credit_loan'):
            extra_fields.append('credit_loan')
        if hasattr(UserModel, 'is_staff'):
            extra_fields.append('is_staff')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
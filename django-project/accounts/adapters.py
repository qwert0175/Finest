from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        
        user_email(user, data.get('email'))
        user_username(user, data.get('username'))
        user.nickname = data.get('nickname')

        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        
        if commit:
            user.save()
        return user

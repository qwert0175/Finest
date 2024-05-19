from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # 필드 추가
        nickname = data.get("nickname")
        gender = data.get("gender")
        age = data.get("age")
        birthday = data.get("birthday")
        salary = data.get("salary")
        asset = data.get("asset")
        debt = data.get("debt")
        deposit = data.get("deposit")
        saving = data.get("saving")
        credit_loan = data.get("credit_loan")
        is_staff = data.get("is_staff")
        profile_image = data.get("profile_image")

        user_email(user, email)
        user_username(user, username)
        
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user.gender = gender
        if age:
            user.age = age  # Direct assignment for integer field
        if birthday:
            user.birthday = birthday
        if salary:
            user.salary = salary
        if asset:
            user.asset = asset
        if debt:
            user.debt = debt
        if deposit:
            user.deposit = deposit
        if saving:
            user.saving = saving
        if credit_loan:
            user.credit_loan = credit_loan
        if is_staff:
            user.is_staff = is_staff
        if profile_image:
            user.profile_image.save(profile_image.name, profile_image, save=False)
        # if deposit:
        #     user_field(user, "deposit", deposit)
        # if saving:
        #     user_field(user, "saving", saving)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)
        if commit:
        # Ability not to commit makes it easier to derive from
        # this adapter by adding
            user.save()
        return user
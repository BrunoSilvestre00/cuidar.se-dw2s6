from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class EmailBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            username = username.lower().strip()
            user = UserModel.objects.get(email__iexact=username)
            return user if user.check_password(password) else None
        except:
            return None
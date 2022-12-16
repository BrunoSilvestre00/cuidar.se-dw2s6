from rest_framework.authentication import TokenAuthentication as RestTokenAuthentication, get_authorization_header
from rest_framework import exceptions
from .models import UserToken


class TokenAuthentication(RestTokenAuthentication):

    model = UserToken

    # def authenticate(self, request):
    #     try:
    #         return super(TokenAuthentication, self).authenticate(request)
    #     except exceptions.AuthenticationFailed as e:
    #         try:
    #             data = str(e)
    #             key = get_authorization_header(request).split()[1]
    #             email = self.get_model().objects.using('read').select_related('user').get(key=key).user.email
    #             data = {'detail': str(e), 'email': email}
    #         except:
    #             pass
    #         finally:
    #             raise exceptions.AuthenticationFailed(data)
    #     except Exception as e:
    #         raise


from django.http import QueryDict
from django.shortcuts import render
from rest_framework import status, parsers, renderers, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import UserToken
from user.permissions import HasAPIAccess
from user.serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = (HasAPIAccess, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        token, created = UserToken.objects.get_or_create(user=user)
        
        data = serializer.data
        data['token'] = token.key
        
        return Response(data, status=status.HTTP_201_CREATED)


class LoginView(APIView):

    permission_classes = (HasAPIAccess,)
    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser, 
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        arr = request.data
        username = arr['email'].lower()
        password = arr['password']
        refact_query_dict = {'username': username, 'password': password}
        new_query_dict = QueryDict('', mutable=True)
        new_query_dict.update(refact_query_dict)

        serializer = self.serializer_class(data=new_query_dict, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = UserToken.objects.get_or_create(user=user)

        data = {
            'user_id': user.id,
            'token': token.key,
            # 'auth': user.token_auth,
        }

        return Response(data)

import random
from rest_framework import serializers
from user.models import User
from rest_framework.exceptions import APIException

class UserAlreadyRegistered(APIException):
    status_code = 400
    default_detail = "User already registered"

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    name = serializers.SerializerMethodField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'name', 'password')
        
    def create(self, validated_data):

        if User.objects.filter(email=validated_data['email']).exists():
            raise UserAlreadyRegistered()

        user_data = validated_data.copy()
        
        print(user_data)
        
        names = user_data['username'].split(' ')
        user_data['first_name'] = names[0]
        user_data['last_name'] = names[1] if len(names) > 1 else ''
        user_data['username'] += user_data['username'].lower().replace(' ', '_') + str(random.randint(10, 101))
        
        return User.objects.create_user(**user_data)
        
    def get_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

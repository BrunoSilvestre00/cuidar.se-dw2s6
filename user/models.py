import base64
import binascii
import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    class Meta:
        db_table = "user"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
    
    @property
    def token_auth(self):
        key = "{0}:{1}".format(self.id, self.auth_token.key)
        return base64.encodebytes(key.encode('utf-8')).decode('utf-8').replace('\n', '')


class Relative(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    birth_date = models.DateField(verbose_name='Data de Nascimento')
    responsable = models.ForeignKey(User, verbose_name='Responsável', on_delete=models.CASCADE)
    
    class Meta:
        db_table='relative'
        verbose_name='Dependente'
        verbose_name_plural='Dependentes'


class ApiToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField("Criado", auto_now_add=True)

    class Meta:
        db_table = "api_tokens"
        verbose_name_plural = "Tokens de API"
        ordering = ['-created']

    def __str__(self):
        return self.name


class UserToken(models.Model):
    key = models.CharField("Key", max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name="Usuário"
    )
    created = models.DateTimeField("Criado", auto_now_add=True)

    class Meta:
        db_table = "user_tokens"
        verbose_name_plural = "Tokens de Usuário"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(UserToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
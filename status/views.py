from django.shortcuts import render
from rest_framework import viewsets

from status.models import Anotation
from status.serializers import AnnotationSerializer
from user.authentication import TokenAuthentication

# Create your views here.
class AnnotationViewSet(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    authentication_classes = (TokenAuthentication,)
    queryset = Anotation.objects.all()
    lookup_field = 'id'
    
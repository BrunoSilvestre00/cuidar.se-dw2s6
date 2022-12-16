from rest_framework import serializers
from status.models import Anotation


class AnnotationSerializer(serializers.ModelSerializer):
    
    category = serializers.CharField(source='category_name')
    status = serializers.CharField(source='status_name')
    
    class Meta:
        model = Anotation
        fields = '__all__'
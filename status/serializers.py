from rest_framework import serializers
from status.models import Anotation


class AnnotationSerializer(serializers.ModelSerializer):
    
    category = serializers.CharField(source='category_name', read_only=True)
    status = serializers.CharField(source='status_name', read_only=True)
    category = serializers.CharField(write_only=True)
    status = serializers.CharField(write_only=True)
    
    class Meta:
        model = Anotation
        fields = '__all__'
from rest_framework import serializers
from .models import TypeBody

class TypeBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeBody
        fields = ['pk', 'type']
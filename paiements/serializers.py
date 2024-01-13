from rest_framework import serializers
from .models import Versement

class VersementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Versement
        fields = '__all__'
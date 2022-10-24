from rest_framework import serializers

from .models import QrGenerator


class QrGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrGenerator
        
        fields = ['id', 'name', 'qr_code_img']
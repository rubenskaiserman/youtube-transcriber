from rest_framework import serializers
from .models import Transcriber_Model_Template

class Transcriber_Serializer_Template(serializers.ModelSerializer):
    class Meta:
        model = Transcriber_Model_Template
        fields = ['email', 'name']
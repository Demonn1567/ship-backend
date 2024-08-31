from rest_framework import serializers
from .models import ParameterSubmission

class ParameterSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterSubmission
        fields = '__all__'

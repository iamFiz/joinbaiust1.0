from rest_framework import serializers

from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    roll = serializers.CharField(
        source='application.details.serial', read_only=True)

    class Meta:
        model = Result
        fields = '__all__'

from rest_framework import serializers
from .models import Visit, Workers, Unit

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('__all__')

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('__all__')


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('__all__')
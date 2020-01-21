from rest_framework import serializers
from .models import Schedule
from rest_framework.serializers import (
    CharField,
    HyperlinkedModelSerializer,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
)


class ScheduleSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Schedule
        fields = '__all__'

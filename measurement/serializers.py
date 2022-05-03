from abc import ABC

from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.Serializer):
	temperature = serializers.FloatField()
	created_at = serializers.DateTimeField()


class SensorDetailSerializer(serializers.ModelSerializer):
	measurements = MeasurementSerializer(read_only=True, many=True)

	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description', 'measurements']

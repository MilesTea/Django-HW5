# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import rest_framework.generics

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorListCreateView(rest_framework.generics.ListCreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer

class SensorRetrieveUpdateView(rest_framework.generics.RetrieveUpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorDetailSerializer

class MeasurementCreateView(rest_framework.generics.CreateAPIView):
	queryset = Measurement.objects.all()
	serializer_class = MeasurementSerializer

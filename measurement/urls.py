from django.urls import path

from measurement import views

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
	path('sensors/', views.SensorListCreateView.as_view()),
	path('sensors/<pk>/', views.SensorRetrieveUpdateView.as_view()),
	path('measurements/', views.MeasurementCreateView.as_view()),
]

from django.urls import path
from .views import SimulatorEndpoint

urlpatterns = [
    path('simulators/', SimulatorEndpoint.as_view(), name='simulator_endpoint'),
]

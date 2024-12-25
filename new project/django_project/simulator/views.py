from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Simulator

class SimulatorEndpoint(APIView):
    def get(self, request):
        simulators = Simulator.objects.all().values()
        return Response(list(simulators))

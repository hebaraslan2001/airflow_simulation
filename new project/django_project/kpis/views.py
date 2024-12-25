from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

class KpiEndpoint(APIView):
    def post(self, request):
        value = request.data.get("value")
        kpi_id = request.data.get("kpi_id")
        result = value + 50 * (value / 10)
        return Response({
            "input_value": value,
            "kpi_id": kpi_id,
            "result": result
        })

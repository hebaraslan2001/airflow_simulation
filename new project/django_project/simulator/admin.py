from django.contrib import admin

# Register your models here.
from .models import Simulator

#admin.site.register(Simulator)
@admin.register(Simulator)
class SimulatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'interval', 'kpi_id')
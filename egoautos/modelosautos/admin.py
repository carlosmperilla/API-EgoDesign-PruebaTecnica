from django.contrib import admin

from .models import ModeloAuto

class ModelosAutosAdmin(admin.ModelAdmin):
    list_display = (
                    'nombre',
                    'anio',
                    'precio',
                    )
    search_fields = (
                    'nombre',
                    'anio',
                    'precio',
                    )
    ordering = (
                'nombre', 
                'anio',
                'precio',
                )
    list_filter = (
                    'nombre',
                    'anio',
                    'precio',
                    )

# Register your models here.
admin.site.register(ModeloAuto, ModelosAutosAdmin)
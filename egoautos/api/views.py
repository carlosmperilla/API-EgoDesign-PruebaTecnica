from rest_framework import viewsets, permissions, filters

from modelosautos.models import ModeloAuto
from .serializers import ModeloAutoSerializer

class ModeloAutoViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Modelos de Autos**.
    ## <span style="color:darkslateblue">Filtros</span>
    Para ordenar de más viejo a más nuevo:  
    > /modelos-autos/?ordering=anio

    Para ordenar de más nuevo a más viejo:  
    > /modelos-autos/?ordering=-anio
    
    Para ordenar de más barato a más costoso:  
    > /modelos-autos/?ordering=precio
    
    Para ordenar de más costoso a más barato:  
    > /modelos-autos/?ordering=-precio

    Para buscar por nombre (puede ser todo el nombre o una parte):
    > /modelos-autos/?search=nombremodelo
    """

    queryset = ModeloAuto.objects.all()
    serializer_class = ModeloAutoSerializer
    filter_backends = [
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       ]
    search_fields = ['nombre', 'anio', 'precio']
    ordering_fields = ['nombre', 'anio', 'precio']
    ordering = ['nombre', 'anio', 'precio']
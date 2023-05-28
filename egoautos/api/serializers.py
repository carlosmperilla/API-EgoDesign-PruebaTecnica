from rest_framework import serializers

from modelosautos.models import ModeloAuto

class ModeloAutoSerializer(serializers.HyperlinkedModelSerializer):
    """
       ModeloAuto serializer class
    """

    class Meta:
        model = ModeloAuto
        fields = ['url', 'nombre', 'anio', 'precio']

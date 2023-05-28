from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ModeloAuto(models.Model):
    nombre =  models.CharField(null=False, blank=False, unique=True, max_length=25, verbose_name="Nombre")
    anio = models.IntegerField(null=False, verbose_name="Año", validators=[MinValueValidator(2000), MaxValueValidator(9999)])
    precio = models.DecimalField(null=False, max_digits=11, decimal_places=2, verbose_name="Precio", validators=[MinValueValidator(0.0), MaxValueValidator(999999999.)])
    
    class Meta:
        verbose_name = "Modelo de Auto"
        verbose_name_plural = "Modelos de Autos"
        ordering = ['nombre', 'anio']

    def __str__(self):
        return self.nombre + ' - ' + str(self.pk)

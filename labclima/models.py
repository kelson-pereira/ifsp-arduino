from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

# Modelo de dados do registro
class Registro(models.Model):
    ident = models.AutoField(primary_key=True)
    datahora = models.DateTimeField(auto_now_add=True)
    nome = models.TextField(max_length=16, blank=True, null=True)
    cep = models.TextField(max_length=9, validators=[MinLengthValidator(9)])
    temperatura = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    umidade = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    pressao = models.IntegerField(null=True, validators=[MaxValueValidator(9999)])

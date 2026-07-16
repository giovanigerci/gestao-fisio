from django.db import models
from profissionais.models import Profissional

# Create your models here.
class Clinica(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome
    
class VinculoClinica(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    valor_por_atendimento = models.DecimalField(max_digits=6, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.profissional} - {self.clinica}"
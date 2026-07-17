from django.db import models
from profissionais.models import Profissional

class Paciente(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True)
    historico_medico = models.TextField(blank=True)

    def __str__(self):
        return self.nome

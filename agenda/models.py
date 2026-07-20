from django.db import models
from clinicas.models import Clinica
from pacientes.models import Paciente
from profissionais.models import Profissional

class Agendamento(models.Model):
    class Status(models.TextChoices):
        AGENDADO = 'AG', 'Agendado'
        REALIZADO = 'RE', 'Realizado'
        CANCELADO = 'CA', 'Cancelado'

    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AGENDADO)
    eh_experimental = models.BooleanField(default=False)
    eh_gratuito = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.paciente} - {self.data} {self.hora_inicio}"
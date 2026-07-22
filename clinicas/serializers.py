from rest_framework import serializers
from .models import Clinica, VinculoClinica

class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = ['id', 'nome', 'endereco', 'telefone']

class VinculoClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinculoClinica
        fields = ['id', 'profissional', 'clinica', 'valor_por_atendimento', 'ativo']
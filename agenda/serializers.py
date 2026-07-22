from rest_framework import serializers
from .models import Agendamento
from clinicas.models import VinculoClinica

class AgendamentoSerializer(serializers.ModelSerializer):
    valor_calculado = serializers.SerializerMethodField()

    class Meta:
        model = Agendamento
        fields = ['id', 'profissional', 'clinica', 'paciente', 'data', 'hora_inicio',
                   'hora_fim', 'status', 'eh_experimental', 'eh_gratuito', 'valor_calculado']

    def get_valor_calculado(self, obj):
        if obj.eh_gratuito:
            return 0
        try:
            vinculo = VinculoClinica.objects.get(profissional=obj.profissional, clinica=obj.clinica)
            return vinculo.valor_por_atendimento
        except VinculoClinica.DoesNotExist:
            return None

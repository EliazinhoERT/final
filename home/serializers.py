from rest_framework import serializers
from .models import CotacoesDasAcoes, Company, Balanco
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
class CotacoesDasAcoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotacoesDasAcoes
        fields = ['date', 'preco_da_acao', 'nome_da_empresa']

class BalancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balanco
        fields = "__all__"

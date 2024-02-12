from django.utils import timezone
from .models import EstatisticasVisualizacao

class EstatisticasMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Obter endereço IP do usuário
        ip_address = request.META.get('REMOTE_ADDR')

        # Atualizar estatísticas de visualização com base no IP
        estatisticas, created = EstatisticasVisualizacao.objects.get_or_create(
            ip_address=ip_address,
            defaults={'total_visualizacoes': 0}
        )
        estatisticas.total_visualizacoes += 1
        estatisticas.save()

        response = self.get_response(request)

        return response
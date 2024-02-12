from django.db.models import Max
from typing import List
from decimal import Decimal
from django.http import JsonResponse
from ninja import NinjaAPI, Path, Query

from datetime import timedelta

import orjson
from ninja.parser import Parser
from django.http import HttpRequest

from .schema import (
    MetricasPorAcaoSchema, DemonstracaoDeFluxoDeCaixaSchema
)

from .models import (
    Noticias,
    Balanco,
    TableDeDivida,
    DemonstracaoDeResultados,
    DemonstracaoDeFluxoDeCaixa,
    IndicadoresDeRentabilidade,
    IndicadoresDeEficiencia,
    IndicadoresDeCrescimento,
    IndicadoresDeEndividamento,
    MetricasPorAccao,
    CotacoesDasAcoes,
    Company,
    Corretoras,
)

from .serializers import (CompanySerializer, CotacoesDasAcoesSerializer)
class ORJSONParser(Parser):
    def parse_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORJSONParser())

@api.get('company/')
def listar_company(request, id=None):
    if id:
        compan = Company.objects.get(id=id)
        serialized_company = {
            "id": compan.id,
            "name": compan.name,
            "abreviatura": compan.abreviatura,
            "sector_de_actuacao": compan.sector_de_actuacao,
            "company_logo": compan.company_logo.url if compan.company_logo else None,  # Obtenha a URL da imagem
            "codigo_isin": compan.codigo_isin,
        }
        return JsonResponse(serialized_company, safe=False)
    else:
        companys = Company.objects.all()
        serialized_companys = []
        for compan in companys:
            serialized_companys.append({
                "id": compan.id,
                "name": compan.name,
                "abreviatura": compan.abreviatura,
                "sector_de_actuacao": compan.sector_de_actuacao,
                "company_logo": compan.company_logo.url if compan.company_logo else None,  # Obtenha a URL da imagem
                "codigo_isin": compan.codigo_isin,
            })
        return JsonResponse(serialized_companys, safe=False)

@api.get('corretoras/')
def listar_corretoras(request, id=None):
    if id:
        corretora = Corretoras.objects.get(id=id)
        serialized_corretora = {
            "id": corretora.id,
            "name": corretora.name,
            "nome_do_phone_1": corretora.nome_do_phone_1,
            "nome_do_phone_2": corretora.nome_do_phone_2,
            "nome_do_phone_3": corretora.nome_do_phone_3,
            "email_1": corretora.email_1,
            "email_2": corretora.email_2,
            "email_3": corretora.email_3,
            "phone_number_1": corretora.phone_number_1,
            "phone_number_2": corretora.phone_number_2,
            "phone_number_3": corretora.phone_number_3,
            "arquivo": corretora.arquivo.url if corretora.arquivo else None,  # Obtenha a URL da imagem
            "outros_arquivos": corretora.outros_arquivos.url if corretora.outros_arquivos else None,  # Obtenha a URL da imagem
            "imagem": corretora.imagem.url if corretora.imagem else None,  # Obtenha a URL da imagem
            "link_da_corretora": corretora.link_da_corretora,
        }
        return JsonResponse(serialized_corretora, safe=False)
    else:
        corretoras = Corretoras.objects.all()
        serialized_corretoras = []
        for corretora in corretoras:
            serialized_corretoras.append({
                "id": corretora.id,
                "name": corretora.name,
                "nome_do_phone_1": corretora.nome_do_phone_1,
                "nome_do_phone_2": corretora.nome_do_phone_2,
                "nome_do_phone_3": corretora.nome_do_phone_3,
                "email_1": corretora.email_1,
                "email_2": corretora.email_2,
                "email_3": corretora.email_3,
                "phone_number_1": corretora.phone_number_1,
                "phone_number_2": corretora.phone_number_2,
                "phone_number_3": corretora.phone_number_3,
                "arquivo": corretora.arquivo.url if corretora.arquivo else None,  # Obtenha a URL da imagem
                "outros_arquivos": corretora.outros_arquivos.url if corretora.outros_arquivos else None,  # Obtenha a URL da imagem
                "imagem": corretora.imagem.url if corretora.imagem else None,  # Obtenha a URL da imagem
                "link_da_corretora": corretora.link_da_corretora,
            })
        return JsonResponse(serialized_corretoras, safe=False)

@api.get("/price-data/")
def get_price_data(request, nome_da_empresa: Query[int] = None):
    queryset = CotacoesDasAcoes.objects.all()

    # Apply filters if nome_da_empresa is provided
    if nome_da_empresa is not None:
        queryset = queryset.filter(nome_da_empresa=nome_da_empresa)

    serializer = CotacoesDasAcoesSerializer(queryset, many=True)
    return serializer.data

@api.get('indicadordeeficiencia/')
def listar_eficiencia(request, empresa_id=None):
    if empresa_id:
        ef = IndicadoresDeEficiencia.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        ef = IndicadoresDeEficiencia.objects.all()
    latest_years = IndicadoresDeEficiencia.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    ef = ef.filter(ano__in=[item['last_year'] for item in latest_years])

    tabela_de_eficiencia = []
    for instance in ef:
        tabela_de_eficiencia.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.name,
            "margem_bruta": '{:,.2f}'.format(instance.margem_bruta()).replace(',', ' '),
            "margin_EBITIDA": instance.margin_EBITIDA(),
            "margin_EBIT": '{:,.2f}'.format(instance.margin_EBIT(),).replace(',', ' '),
            "margin_Liquida": '{:,.2f}'.format(instance.margin_Liquida()).replace(',', ' '),
        })

    return JsonResponse(tabela_de_eficiencia, safe=False)

@api.get('indicadoresdecrescimento/')
def listar_crescimento(request, empresa_id=None):
    if empresa_id:
        crescimento = IndicadoresDeCrescimento.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        crescimento = IndicadoresDeCrescimento.objects.all()
    latest_years = IndicadoresDeCrescimento.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    crescimento = crescimento.filter(ano__in=[item['last_year'] for item in latest_years])

    tabela_de_crescimento = []
    for instance in crescimento:
        tabela_de_crescimento.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.name,
            "CAGR_Receita_5A": '{:,.2f}'.format(instance.CAGR_Receita_5A()).replace(',', ' '),
            "CAGR_Lucro_5A": '{:,.2f}'.format(instance.CAGR_Lucro_5A()).replace(',', ' '),
        })
    return JsonResponse(tabela_de_crescimento, safe=False)

@api.get('indicadordeendividamento/')
def listar_endivadamento(request, empresa_id=None):
    if empresa_id:
        envidamento = IndicadoresDeEndividamento.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        envidamento = IndicadoresDeEndividamento.objects.all()
    latest_years = IndicadoresDeEndividamento.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    envidamento = envidamento.filter(ano__in=[item['last_year'] for item in latest_years])

    tabela_de_endividamento = []
    for instance in envidamento:
        tabela_de_endividamento.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.name,
            "Liquidez_Corrente": '{:,.2f}'.format(instance.Liquidez_Corrente()).replace(',', ' '),
            "Liquidez_Seca": '{:,.2f}'.format(instance.Liquidez_Seca()).replace(',', ' '),
            "Liquidez_Geral": '{:,.2f}'.format(instance.Liquidez_Geral()).replace(',', ' '),
            "Divida_or_Activo_Total": '{:,.2f}'.format(instance.Divida_or_Activo_Total()).replace(',', ' '),
            "Divida_Patrimonio_Liquido": '{:,.2f}'.format(instance.Divida_Patrimonio_Liquido()).replace(',', ' '),
            "Divida_Liquido_EBITD": instance.Divida_Liquido_EBITD(),
            "Divida_Liquido_EBITDA": instance.Divida_Liquido_EBITDA(),
            "Divida_Liquido_Lucro_Liquido": '{:,.2f}'.format(instance.Divida_Liquido_Lucro_Liquido()).replace(',', ' '),
            "Divida_Bruta_Lucro_Liquido": '{:,.2f}'.format(instance.Divida_Bruta_Lucro_Liquido()).replace(',', ' '),
            "Passivo_Activo": '{:,.2f}'.format(instance.Passivo_Activo()).replace(',', ' '),
        })
    return JsonResponse(tabela_de_endividamento, safe=False)

@api.get('cotacoes/')
def listar_cotacoes(request, empresa_id=None):
    if empresa_id:
        # Se um ID de empresa for fornecido, filtre os dados apenas para essa empresa
        instances = TableDeDivida.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        instances = TableDeDivida.objects.all()
    latest_years = TableDeDivida.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    instances = instances.filter(ano__in=[item['last_year'] for item in latest_years])

    tabela_de_divida = []
    for instance in instances:
        serialized_company = CompanySerializer(instance.nome_da_empresa).data
        tabela_de_divida.append({
            'id': instance.id,
            'ano': instance.ano,
            'nome_da_empresa': serialized_company,
            'divida_bruta': '{:,.2f}'.format(instance.divida_bruta).replace(',', ' '),
            'divida_liquida': '{:,.2f}'.format(instance.divida_liquida()).replace(',', ' '),
        })

    return JsonResponse(tabela_de_divida, safe=False)


@api.get('indicadorderentabilidade/')
def lista_rentabilidade(request, empresa_id=None):
    if empresa_id:
        # Se um ID de empresa for fornecido, filtre os dados apenas para essa empresa
        rentabilidade = IndicadoresDeRentabilidade.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        rentabilidade = IndicadoresDeRentabilidade.objects.all()

    latest_years = IndicadoresDeRentabilidade.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    rentabilidade = rentabilidade.filter(ano__in=[item['last_year'] for item in latest_years])

    serialized_rentabilidade = []
    for instance in rentabilidade:
        serialized_rentabilidade.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.name,
            "ROA": '{:,.2f}'.format(instance.ROA()).replace(',', ' '),
            "ROE": '{:,.2f}'.format(instance.ROE()).replace(',', ' '),
            "Roic": '{:,.2f}'.format(instance.Roic()).replace(',', ' '),
            "Giro_dos_Activos": '{:,.2f}'.format(instance.Giro_dos_Activos()).replace(',', ' '),
        })
    return JsonResponse(serialized_rentabilidade, safe=False)

@api.get('noticias/')
def listar_noticias(request, id=None):
    if id:
        noticia = Noticias.objects.get(id=id)
        serialized_noticia = {
            "id": noticia.id,
            "date": noticia.date.strftime('%Y-%m-%d %A'),
            "titulo": noticia.titulo,
            "noticia": noticia.noticia,
            "corpo": noticia.corpo,
            "imagens": noticia.imagens.url if noticia.imagens else None
        }
        return JsonResponse(serialized_noticia, safe=False)
    else:
        noticias = Noticias.objects.all()
        serialized_noticias = []
        for noticia in noticias:
            serialized_noticias.append({
                "id": noticia.id,
                "date": noticia.date.strftime('%Y-%m-%d %A'),
                "titulo": noticia.titulo,
                "noticia": noticia.noticia,
                "corpo": noticia.corpo,
                "imagens": noticia.imagens.url if noticia.imagens else None,
            })
        return JsonResponse(serialized_noticias, safe=False)

@api.get('cotacaomensal/')
def lista_cotacaomensal(request, empresa_id=None):
    if empresa_id:
        # Se um ID de empresa for fornecido, filtre os dados apenas para essa empresa
        cotacao1 = CotacoesDasAcoes.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        # Caso contrário, obtenha todos os dados
        cotacao1 = CotacoesDasAcoes.objects.all()

    latest_dates = CotacoesDasAcoes.objects.values('nome_da_empresa_id').annotate(last_date=Max('date'))

        # Filtrar instâncias para incluir apenas os dados mais recentes de cada empresa
    cotacao1 = cotacao1.filter(date__in=[item['last_date'] for item in latest_dates])

    serialized_cotacao = []
    for instance in cotacao1:
        serialized_cotacao.append({
            "nome_da_empresa": instance.nome_da_empresa.name,
            "preco_da_acao": '{:,.2f}'.format(instance.preco_da_acao).replace(',', ' '),
            "Variacao_Mensal": instance.Variacao_Mensal(),
        })
    return JsonResponse(serialized_cotacao, safe=False)


@api.get('cotacoess/')
def lista_cotacoes(request, empresa_id=None):
    if empresa_id:
        # Se um ID de empresa for fornecido, filtre os dados apenas para essa empresa
        cotacao = CotacoesDasAcoes.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        # Caso contrário, obtenha todos os dados
        cotacao = CotacoesDasAcoes.objects.all()

    latest_dates = CotacoesDasAcoes.objects.values('nome_da_empresa_id').annotate(last_date=Max('date'))

        # Filtrar instâncias para incluir apenas os dados mais recentes de cada empresa
    cotacao = cotacao.filter(date__in=[item['last_date'] for item in latest_dates])

    serialized_cotacao = []
    for instance in cotacao:
        serialized_cotacao.append({
            "id": instance.id,
            "date": instance.date,
            "nome_da_empresa": instance.nome_da_empresa.name,
            "preco_da_acao": '{:,.2f}'.format(instance.preco_da_acao).replace(',', ' '),
            "Valor_Do_Mercado": '{:,.2f}'.format(instance.Valor_Do_Mercado()).replace(',', ' '),
            "Variacao_Diaria": '{:,.2f}'.format(instance.Variacao_Diaria()).replace(',', ' '),
            "EV": '{:,.2f}'.format(instance.EV()).replace(',', ' '),
            "Variacao_Mensal": instance.Variacao_Mensal(),
            "Variacao_Semestral": instance.Variacao_Semestral(),
            "P_L": instance.P_L(),
            "P_EBIT": instance.P_EBIT(),
            "P_EBITDA": instance.P_EBITDA(),
            "P_Activos": instance.P_Activos(),
            "P_VPA": instance.P_VPA(),
            "PSR": instance.PSR(),
            "P_Capital_de_Giro_Liquido": instance.P_Capital_de_Giro_Liquido(),
            "P_Capital_de_Giro": instance.P_Capital_de_Giro(),
            "EV_EBIT": instance.EV_EBIT(),
            "EV_EBITDA": instance.EV_EBITDA(),
            "Volume_de_negociacao": '{:,.2f}'.format(instance.Volume_de_negociacao()).replace(',', ' '),
        })
    return JsonResponse(serialized_cotacao, safe=False)

@api.get('balanco/')
def lista_balanco(request, empresa_id=None):
    if empresa_id:
        bal = Balanco.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        bal = Balanco.objects.all()
    latest_years = Balanco.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    bal = bal.filter(ano__in=[item['last_year'] for item in latest_years])

    serialized_balanco = []
    for instance in bal:
        serialized_balanco.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.id,
            "activo_corrente": '{:,.2f}'.format(instance.activo_corrente).replace(',', ' '),
            "caixa": '{:,.2f}'.format(instance.caixa).replace(',', ' '),
            "inventarios": '{:,.2f}'.format(instance.inventarios).replace(',', ' '),
            "activo_nao_corrente": '{:,.2f}'.format(instance.activo_nao_corrente).replace(',', ' '),
            "total_de_activo": '{:,.2f}'.format(instance.total_de_activo()).replace(',', ' '),
            "passivo_corrente": '{:,.2f}'.format(instance.passivo_corrente).replace(',', ' '),
            "passivo_nao_corrente": '{:,.2f}'.format(instance.passivo_nao_corrente).replace(',', ' '),
            "total_de_passivo": '{:,.2f}'.format(instance.total_de_passivo()).replace(',', ' '),
            "capital_social": '{:,.2f}'.format(instance.capital_social).replace(',', ' '),
            "reservas_nao_distribuidas": '{:,.2f}'.format(instance.reservas_nao_distribuidas).replace(',', ' '),
            "premio_de_emissao": '{:,.2f}'.format(instance.premio_de_emissao).replace(',', ' '),
            "lucros_acumulados": '{:,.2f}'.format(instance.lucros_acumulados).replace(',', ' '),
            "disconto_de_premio_das_acoes_proprias": '{:,.2f}'.format(instance.disconto_de_premio_das_acoes_proprias).replace(',', ' '),
            "resultados_transitado": '{:,.2f}'.format(instance.resultados_transitado).replace(',', ' '),
            "resultados_de_exercicio": '{:,.2f}'.format(instance.resultados_de_exercicio).replace(',', ' '),
            "lucros_acumulados_geral": '{:,.2f}'.format(instance.lucros_acumulados_geral()).replace(',', ' '),
            "total_do_capital_proprio": '{:,.2f}'.format(instance.total_do_capital_proprio()).replace(',', ' '),
            "total_do_passvo_e_capital_proprio": '{:,.2f}'.format(instance.total_do_passvo_e_capital_proprio()).replace(',', ' '),
        })
    return JsonResponse(serialized_balanco, safe=False)

@api.get('demostracaoderesultados/')
def lista_resultados(request, empresa_id=None):
    if empresa_id:
        resultados = DemonstracaoDeResultados.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        resultados = DemonstracaoDeResultados.objects.all()
    latest_years = DemonstracaoDeResultados.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    resultados = resultados.filter(ano__in=[item['last_year'] for item in latest_years])

    serialized_resultados = []
    for instance in resultados:
        serialized_resultados.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.id,
            "vendas": '{:,.2f}'.format(instance.vendas).replace(',', ' '),
            "lucros_bruto": '{:,.2f}'.format(instance.lucros_bruto).replace(',', ' '),
            "EBITDA": '{:,.2f}'.format(instance.EBITIDA).replace(',', ' '),
            "EBIT": '{:,.2f}'.format(instance.EBIT).replace(',', ' '),
            "lucro_antes_de_imposto": '{:,.2f}'.format(instance.lucro_antes_de_imposto).replace(',', ' '),
            "impostos": '{:,.2f}'.format(instance.impostos()).replace(',', ' '),
            "lucro_liquido_depois_de_imposto": '{:,.2f}'.format(instance.lucro_liquido_depois_de_imposto).replace(',', ' '),
            "dividendo_declarados_e_pagos": '{:,.2f}'.format(instance.dividendo_declarados_e_pagos).replace(',', ' '),
            "numero_medio_ponderado_de_acoes": '{:,.2f}'.format(instance.numero_medio_ponderado_de_acoes).replace(',', ' '),
            "lucro_por_acao": '{:,.2f}'.format(instance.lucro_por_acao()).replace(',', ' '),
            "dividendo_por_acao": '{:,.2f}'.format(instance.dividendo_por_acao()).replace(',', ' '),
        })
    return JsonResponse(serialized_resultados, safe=False)

@api.get('demostracaodefluxo/')
def lista_fluxo(request, empresa_id=None):
    if empresa_id:
        fluxodecaixa = DemonstracaoDeFluxoDeCaixa.objects.filter(nome_da_empresa_id=empresa_id)
    else:
        fluxodecaixa = DemonstracaoDeFluxoDeCaixa.objects.all()
    latest_years = DemonstracaoDeFluxoDeCaixa.objects.values('nome_da_empresa_id').annotate(last_year=Max('ano'))
    fluxodecaixa = fluxodecaixa.filter(ano__in=[item['last_year'] for item in latest_years])

    serialized_fluxodecaixa = []
    for instance in fluxodecaixa:
        serialized_fluxodecaixa.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.id,
            "fundos_gerados_das_actividades_operacionais": '{:,.2f}'.format(instance.fundos_gerados_das_actividades_operacionais).replace(',', ' '),
            "fundos_utilizados_em_actividades_de_investimento": '{:,.2f}'.format(instance.fundos_utilizados_em_actividades_de_investimento).replace(',', ' '),
            "fundos_introduzidos_atraves_de_actividades_de_financiamento": '{:,.2f}'.format(instance.fundos_introduzidos_atraves_de_actividades_de_financiamento).replace(',', ' '),
            "acrescimo_ou_decrescimo_em_caixa_e_equivalentes_de_caixa": '{:,.2f}'.format(instance.acrescimo_ou_decrescimo_em_caixa_e_equivalentes_de_caixa).replace(',', ' '),
            "fluxo_de_caixa": instance.fluxo_de_caixa(),
        })
    return JsonResponse(serialized_fluxodecaixa, safe=False)

@api.get('metricasporacao/', response=List[MetricasPorAcaoSchema])
def lista_metricasporacao(request, empresa: Query[str] = None):
    metricas = MetricasPorAccao.objects.all()

    # Adicione lógica de filtragem por empresa, se necessário
    if empresa:
        metricas = MetricasPorAccao.filter(nome_da_empresa__nome=empresa)

    serialized_metricas = []
    for instance in metricas:
        serialized_metricas.append({
            "id": instance.id,
            "ano": instance.ano,
            "nome_da_empresa": instance.nome_da_empresa.id,
            "LPA": '{:,.2f}'.format(instance.LPA()).replace(',', ' '),
            "VPL": '{:,.2f}'.format(instance.VPL()).replace(',', ' '),
            "Activos": '{:,.2f}'.format(instance.Activos()).replace(',', ' '),
            "Vendas_Liquidas": '{:,.2f}'.format(instance.Vendas_Liquidas()).replace(',', ' '),
            "Capital_de_Giro": '{:,.2f}'.format(instance.Capital_de_Giro()).replace(',', ' '),
            "Capital_de_Giro_Liquido": '{:,.2f}'.format(instance.Capital_de_Giro_Liquido()).replace(',', ' '),
            "P_L": instance.P_L(),
            "P_VPA": instance.P_VPA(),
            "P_EBITDA": instance.P_EBITDA(),
            "P_ACTIVO": instance.P_ACTIVO(),
            "EBIT_ACTIVOS": instance.EBIT_ACTIVOS(),
            "Dividend_Yield": '{:,.2f}'.format(instance.Dividend_Yield()).replace(',', ' '),
            "PSR": instance.PSR(),
            "P_Capital_De_Giro": instance.P_Capital_De_Giro(),
            "P_Capital_De_Giro_Liquido": instance.P_Capital_De_Giro_Liquido(),
        })
    return serialized_metricas

def get_min_max(arr: List[Decimal]) -> tuple[Decimal, Decimal]:
    arr = sorted(arr)
    min_value, max_value = arr[0], float(arr[-1])
    max_value_formatted = format(max_value, '.2f')
    return min_value, max_value_formatted

def get_value_from_table(func):
    try:
        val = round(float(func), 4)
    except Exception as e:
        val = 0
    return val

# @api.get("/precos-metricas-por-acao/{nome_da_empresa}/{start_year}/{end_year}")
# def precos_metricas_por_acao(request, nome_da_empresa: str, start_year: int, end_year: int):
#     try:
#         company = Company.objects.get(name=nome_da_empresa)
#         metricas_por_acao = MetricasPorAccao.objects.filter(
#             nome_da_empresa=company, ano__gte=start_year,
#             ano__lte=end_year)
#         P_L_values = []
#         P_VPA_values = []
#         P_EBITDA_values = []
#         P_ACTIVO_values = []
#         PSR_values = []
#         P_Capital_De_Giro_values = []
#         Dividend_Yield_values = []
#         anos = []
#         end_year_val = None
#         try:
#             start_year_val = metricas_por_acao.first().ano
#         except Exception as e:
#             start_year_val = None
#
#         for metrica in metricas_por_acao:
#             anos.append(metrica.ano)
#             P_L_values.append(get_value_from_table(metrica.P_L()))
#             P_VPA_values.append(get_value_from_table(metrica.P_VPA()))
#             P_EBITDA_values.append(get_value_from_table(metrica.P_EBITDA()))
#             P_ACTIVO_values.append(get_value_from_table(metrica.P_ACTIVO()))
#             PSR_values.append(get_value_from_table(metrica.PSR()))
#             P_Capital_De_Giro_values.append(get_value_from_table(metrica.P_Capital_De_Giro()))
#             Dividend_Yield_values.append(get_value_from_table(metrica.Dividend_Yield()))
#
#             end_year_val = metrica.ano
#
#         try:
#             all_values = P_L_values
#             min_value, max_value = get_min_max(all_values)
#         except Exception as e:
#             min_value, max_value = None, None
#
#     except CotacoesDasAcoes.DoesNotExist:
#         anos = []
#         min_value = 0
#         max_value = 0
#         P_L_values = []
#         P_VPA_values = []
#         P_EBITDA_values = []
#         P_ACTIVO_values = []
#         PSR_values = []
#         P_Capital_De_Giro_values = []
#         Dividend_Yield_values = []
#         start_year_val = None
#         end_year_val = None
#
#     try:
#         indicadores_de_rentabilidade = IndicadoresDeRentabilidade.objects.filter(
#             nome_da_empresa=company, ano__gte=start_year,
#             ano__lte=end_year)
#         anos_indicadores_de_rentabilidade = []
#         ROA_values = []
#         ROE_values = []
#         Roic_values = []
#         Giro_dos_Activos_values = []
#         for indicador in indicadores_de_rentabilidade:
#             anos_indicadores_de_rentabilidade.append(indicador.ano)
#             ROA_values.append(get_value_from_table(indicador.ROA()))
#             ROE_values.append(get_value_from_table(indicador.ROE()))
#             Roic_values.append(get_value_from_table(indicador.Roic()))
#
#     except Exception as e:
#         anos_indicadores_de_rentabilidade = []
#         ROA_values = []
#         ROE_values = []
#         Roic_values = []
#
#     # Restante do código continua...
#
#     return JsonResponse({
#         'min_value': min_value,
#         'max_value': max_value,
#         'anos': anos,
#         'P_L_values': P_L_values,
#         'P_VPA_values': P_VPA_values,
#         'P_EBITDA_values': P_EBITDA_values,
#         'P_ACTIVO_values': P_ACTIVO_values,
#         'PSR_values': PSR_values,
#         'P_Capital_De_Giro_values': P_Capital_De_Giro_values,
#         'Dividend_Yield_values': Dividend_Yield_values,
#         'anos_indicadores_de_rentabilidade': anos_indicadores_de_rentabilidade,
#         'ROA_values': ROA_values,
#         'ROE_values': ROE_values,
#         'Roic_values': Roic_values,
#         # Adicione as demais variáveis aqui...
#     })


# @api.get("/preco-de-acao/{nome_da_empresa}/{start_date}/{end_date}")
# def preco_de_acao(request, nome_da_empresa: str, start_date: str, end_date: str):
#     try:
#         start_date_val = None
#         end_date_val = None
#         min_value = None
#         max_value = None
#         company = Company.objects.get(name=nome_da_empresa)
#         cotacoes = CotacoesDasAcoes.objects.filter(
#             nome_da_empresa=company, date__gte=start_date,
#             date__lte=end_date)
#         dates = []
#         prices = []
#         start_date_val = cotacoes.first().date
#         for cot in cotacoes:
#             dates.append(cot.date)
#             end_date_val = cot.date
#             prices.append(float(cot.preco_da_acao))
#
#     except CotacoesDasAcoes.DoesNotExist:
#         dates = []
#         prices = []
#         min_value = None
#         max_value = None
#         start_date_val = None
#         end_date_val = None
#
#     return JsonResponse({
#         'dates': dates,
#         'prices': prices,
#         'start_date_val': start_date_val,
#         'end_date_val': end_date_val
#     })

@api.get("variacoes-periodicas/{empresa_id}")
def variacoes_periodicas(request, empresa_id: int):
    try:
        start_date_val = None
        end_date_val = None
        company = Company.objects.get(id=empresa_id)

        # Obtendo a última data em CotacoesDasAcoes para a empresa específica
        ultima_data = CotacoesDasAcoes.objects.filter(
            nome_da_empresa=company
        ).latest('date').date

        # Definindo a data de término como a última data
        end_date_obj = ultima_data

        # Definindo a data de início como 12 meses antes da data de término
        start_date_12_months_ago = end_date_obj - timedelta(days=365)

        cotacoes = CotacoesDasAcoes.objects.filter(
            nome_da_empresa=company, date__gte=start_date_12_months_ago,
            date__lte=end_date_obj)

        precos_da_acao = []
        dates = []
        start_date_val = cotacoes.first().date

        for cot in cotacoes:
            dates.append(cot.date)
            precos_da_acao.append(cot.preco_da_acao)

        end_date_val = cot.date

        min_value, max_value = get_min_max(precos_da_acao)

        # Ajustando o valor de 'start_date_val' para a data de início real
        start_date_val = start_date_12_months_ago

    except CotacoesDasAcoes.DoesNotExist:
        dates = []
        min_value = 0
        max_value = 0
        start_date_val = None
        end_date_val = None

    return JsonResponse({'data': [{
        'min_value': min_value,
        'max_value': max_value,
        'start_date_val': start_date_val,
        'end_date_val': end_date_val,
    }]})

# @api.get("/valor-do-mercado-ev/{nome_da_empresa}/{start_date}/{end_date}")
# def valor_do_mercado_and_ev(request, nome_da_empresa: str, start_date: str, end_date: str):
#     try:
#         start_date_val = None
#         end_date_val = None
#         company = Company.objects.get(name=nome_da_empresa)
#         cotacoes = CotacoesDasAcoes.objects.filter(
#             nome_da_empresa=company, date__gte=start_date,
#             date__lte=end_date)
#         market_values = []
#         e_v_values = []
#         dates = []
#         start_date_val = cotacoes.first().date
#         for cot in cotacoes:
#             dates.append(cot.date)
#             try:
#                 market_values.append(float(cot.Valor_Do_Mercado()))
#             except Exception as e:
#                 market_values.append(0)
#
#             try:
#                 e_v_values.append(float(cot.EV()))
#             except Exception as e:
#                 e_v_values.append(0)
#
#             end_date_val = cot.date
#
#         all_values = market_values + e_v_values
#         min_value, max_value = get_min_max(all_values)
#
#     except CotacoesDasAcoes.DoesNotExist:
#         dates = []
#         min_value = 0
#         max_value = 0
#         market_values = []
#         e_v_values = []
#         start_date_val = None
#         end_date_val = None
#
#     return JsonResponse({
#         'min_value': min_value,
#         'max_value': max_value,
#         'dates': dates,
#         'market_values': market_values,
#         'e_v_values': e_v_values,
#         'start_date_val': start_date_val,
#         'end_date_val': end_date_val
#     })

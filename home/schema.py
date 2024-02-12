from ninja import Schema
from datetime import date
from typing import List, Optional

class CotacoesDasAcoesSchema(Schema):
    id: int
    date: date
    nome_da_empresa: str
    preco_da_acao: Optional[float]
    Valor_Do_Mercado: Optional[float]
    Variacao_Diaria: Optional[float]
    EV: Optional[float]
    Variacao_Mensal: Optional[float]
    Variacao_Semestral: Optional[float]
    # P_L: Optional[float]
    # P_EBIT: Optional[float]
    # P_EBITDA: Optional[float]
    # P_Activos: Optional[float]
    # P_VPA: Optional[float]
    # PSR: Optional[float]
    # P_Capital_de_Giro_Liquido: Optional[float]
    # P_Capital_de_Giro: Optional[float]
    # EV_EBIT: Optional[float]
    # EV_EBITDA: Optional[float]

class IndicadoresDeRentabilidadeSchema(Schema):
    id: int
    ano: int
    nome_da_empresa: int
    ROA: Optional[float]
    ROE: float
    Roic: float
    Giro_dos_Activos: Optional[float]

class DemonstracaoDeFluxoDeCaixaSchema(Schema):
    id: int
    ano: int
    nome_da_empresa: int
    fundos_gerados_das_actividades_operacionais: float
    fundos_utilizados_em_actividades_de_investimento: float
    fundos_introduzidos_atraves_de_actividades_de_financiamento: float
    acrescimo_ou_decrescimo_em_caixa_e_equivalentes_de_caixa: float
    fluxo_de_caixa: float
class MetricasPorAcaoSchema(Schema):
    id: int
    ano: int
    nome_da_empresa: int
    LPA: Optional[float]
    VPL: Optional[float]
    Activos: Optional[float]
    Vendas_Liquidas: Optional[float]
    Capital_de_Giro: Optional[float]
    Capital_de_Giro_Liquido: Optional[float]
    P_L: Optional[float]
    P_VPA: Optional[float]
    P_EBITDA: Optional[float]
    P_ACTIVO: Optional[float]
    EBIT_ACTIVOS: Optional[float]
    Dividend_Yield: Optional[float]
    PSR: Optional[float]
    P_Capital_De_Giro: Optional[float]
    P_Capital_De_Giro_Liquido: Optional[float]
class CotacoesSchema(Schema):
    id:int
    date: date
    nome_da_empresa: str
    preco_da_acao: float
    Valor_Do_Mercado: float
    EV: float
    Variacao_Diaria: float
    Variacao_Semanal: float
    Variacao_Mensal: float
    Variacao_Semestral: float
    P_L: float
    P_EBIT: float
    P_EBITDA: float
    P_Activos: float
    P_VPA: float
    PSR: float
    P_Capital_de_Giro_Liquido: float
    P_Capital_de_Giro: float
    EV_EBIT: float
    EV_EBITDA: float

class DemostracaoDeResultadosSchema(Schema):
    id: int
    ano: int
    nome_da_empresa: int
    vendas: float
    lucros_bruto: float
    EBITDA: float
    EBIT: float
    lucro_antes_de_imposto: float
    impostos: float
    lucro_liquido_depois_de_imposto: float
    dividendo_declarados_e_pagos: float
    numero_medio_ponderado_de_acoes: float
    lucro_por_acao: float
    dividendo_por_acao: float
class BalancoSchema(Schema):
    id: int
    ano: int
    nome_da_empresa: int
    activo_corrente: float
    caixa: float
    inventarios: float
    activo_nao_corrente: float
    total_de_activo: float
    passivo_corrente: float
    passivo_nao_corrente: float
    total_de_passivo: float
    capital_social: float
    reservas_nao_distribuidas: float
    premio_de_emissao: float
    lucros_acumulados: float
    disconto_de_premio_das_acoes_proprias: float
    resultados_transitado: float
    resultados_de_exercicio: float
    lucros_acumulados_geral: float
    total_do_capital_proprio: float
    total_do_passvo_e_capital_proprio: float
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (
    UserProfile,
    Corretoras,
    Client,
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
    Noticias,
    EstatisticasVisualizacao,
)
from .forms import (
    CotacoesDasAcoesForm,
)

admin.site.register(EstatisticasVisualizacao)

def format_value(value, symbol="MZN"):
    if value is None:
        return "Sem registo"
    if value == 0:
        return "Sem registo"
    if symbol == "MZN":
        return mark_safe(f"{symbol} {value}")
    return mark_safe(f"{value}%")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "fullname", "is_member", "contact", "location", "view_details")
    list_editable = ("is_member",)

    def view_details(self, obj):
        return mark_safe(
            f"""
			<a href="/admin/auth/user/{obj.user.id}/change/"
				style="font-size:17px;">&#128065;</a>
			"""
        )

    view_details.short_description = "View Details"

    def fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    fullname.short_description = "Name"

@admin.register(Corretoras)
class CorretorasAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "name",
                    "email_1",
                    "email_2",
                    "email_3",
                    "nome_do_phone_1",
                    "nome_do_phone_2",
                    "nome_do_phone_3",
                    "phone_number_1",
                    "phone_number_2",
                    "phone_number_3",
                    "arquivo",
                    "outros_arquivos",
                    "imagem",
                    "mostrar_logo",
                    "link_da_corretora")
    list_editable = ("name",
                     "email_1",
                     "email_2",
                     "email_3",
                     "nome_do_phone_1",
                     "nome_do_phone_2",
                     "nome_do_phone_3",
                     "arquivo",
                     "outros_arquivos",
                     "link_da_corretora",
                     "imagem")
    def mostrar_logo(self, obj):
        img_path = obj.imagem.url
        return mark_safe(
            f"""
            <a href="#" target="_blank">
                <img src="{img_path}" height="100px" width="100px">
            </a>
            """
        )
    mostrar_logo.short_description = "Imagem Logo"

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "abreviatura", "sector_de_actuacao", "company_logo", "codigo_isin", "show_logo")
    list_editable = ("sector_de_actuacao", "company_logo", "codigo_isin")
    def show_logo(self, obj):
        img_path = obj.company_logo.url
        return mark_safe(
            f"""
    		<a href="#" target="_blank">
    			<img src="{img_path}" height="100px" width="100px">
    		</a>
    	"""
        )

    show_logo.short_description = "Image Logo"

@admin.register(Noticias)
class Noticiasadmin(admin.ModelAdmin):
    list_display = [
        "id",
        "date",
        "titulo",
        "noticia",
        "corpo",
        "sector_da_noticia",
        "imagens",
    ]
    list_editable = ["imagens", "sector_da_noticia"]
    list_filter = ["titulo"]
    search_fields = ["titulo"]
    date_hierarchy = "date"

@admin.register(CotacoesDasAcoes)
class CotacoesDasAcoesdmin(admin.ModelAdmin):
    form = CotacoesDasAcoesForm
    list_display = [
        "id",
        "date",
        "nome_da_empresa",
        "preco_da_acao",
        "numero_de_accoes_negociadas",
        "Valor_Do_Mercado",
        "Volume_de_negociacao",
        "EV",
        "Variacao_Diaria",
        "Variacao_Semanal",
        "Variacao_Mensal",
        "Variacao_Semestral_",
        "P_L",
        "P_EBIT",
        "P_EBITDA",
        "P_Activos",
        "P_VPA",
        "PSR",
        "P_Capital_de_Giro_Liquido",
        "P_Capital_de_Giro",
        "EV_EBIT",
        "EV_EBITDA",
    ]

    list_per_page = 50
    list_filter = [
        "nome_da_empresa",
    ]
    search_fields = [
        "nome_da_empresa",
    ]
    date_hierarchy = "date"

    def Variacao_Semestral_(self, obj):
        if obj.Variacao_Semestral() is None:
            return "Sem registo"
        return mark_safe(f"{obj.Variacao_Semestral()}%")

    Variacao_Semestral_.short_description = "Variacao Semestral"

    def Variacao_Mensal_(self, obj):
        if obj.Variacao_Mensal() is None:
            return "Sem registo"
        # if obj.Variacao_Mensal() == 0:
        # 	return 'Sem registo'
        return mark_safe(f"{obj.Variacao_Mensal()}%")

    Variacao_Mensal_.short_description = "Variacao Mensal"

    def Variacao_Semanal_(self, obj):
        if obj.Variacao_Semanal() is None:
            return "Sem registo"
        # if obj.Variacao_Semanal() == 0:
        # 	return 'Sem registo'
        return mark_safe(f"{obj.Variacao_Semanal()}%")

    Variacao_Semanal_.short_description = "Variacao Semanal"

    def Variacao_Diaria_(self, obj):
        if obj.Variacao_Diaria() is None:
            return "Sem registo"
        # if obj.Variacao_Diaria() == 0:
        # 	return 'Sem registo'
        return mark_safe(f"{obj.Variacao_Diaria()}%")

    Variacao_Diaria_.short_description = "Variacao Diaria"

    def P_EBIT(self, obj):
        if obj.P_EBIT() is None:
            return "Sem registo"
        if obj.P_EBIT() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.P_EBIT()}")

    P_EBIT.short_description = "P EBIT"

    def P_EBITDA(self, obj):
        if obj.P_EBITDA() is None:
            return "Sem registo"
        if obj.P_EBITDA() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.P_EBITDA()}")
    P_EBITDA.short_description = "P EBITDA"

    def P_Activos(self, obj):
        if obj.P_Activos() is None:
            return "Sem registo"
        if obj.P_Activos() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.P_Activos()}")
    P_Activos.short_description = "P Activos"


    def EV_(self, obj):
        if obj.EV() is None:
            return "Sem registo"
        if obj.EV() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.EV()}")

    EV_.short_description = "EV"

    def Valor_Do_Mercado_(self, obj):
        if obj.Valor_Do_Mercado() is None:
            return "Sem registo"
        if obj.Valor_Do_Mercado() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Valor_Do_Mercado()}")

    Valor_Do_Mercado_.short_description = "Valor Do Mercado"


@admin.register(MetricasPorAccao)
class MetricasPorAccaoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "LPA_",
        "VPL_",
        "EBIT_Func",
        "EBITDA_Func",
        "Activos_",
        "Vendas_Liquidas_",
        "Capital_de_Giro_",
        "Capital_de_Giro_Liquido_",
        "P_L_",
        "P_VPA_",
        "P_EBITDA_",
        "P_ACTIVO_",
        "EBIT_ACTIVOS_",
        "Dividend_Yield_",
        "PSR_",
        "P_Capital_De_Giro_",
        "P_Capital_De_Giro_Liquido_",
    ]
    list_filter = ["nome_da_empresa"]

    def P_Capital_De_Giro_Liquido_(self, obj):
        if obj.P_Capital_De_Giro_Liquido() is None:
            return "Sem registo"
        if obj.P_Capital_De_Giro_Liquido() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.P_Capital_De_Giro_Liquido()}")

    P_Capital_De_Giro_Liquido_.short_description = "P Capital De Giro Liquido"

    def P_Capital_De_Giro_(self, obj):
        # value = format_value(obj.P_Capital_De_Giro())
        # return value
        if obj.P_Capital_De_Giro() is None:
            return "Sem registo"
        if obj.P_Capital_De_Giro() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.P_Capital_De_Giro()}")

    P_Capital_De_Giro_.short_description = "P Capital De Giro"

    def PSR_(self, obj):
        if obj.PSR() is None:
            return "Impossivel de calcular"
        if obj.PSR() == 0:
            return 0.0
        return mark_safe(f"MZN {obj.PSR()}")

    PSR_.short_description = "PSR"

    def Dividend_Yield_(self, obj):
        if obj.Dividend_Yield() is None:
            return "Sem registo"
        if obj.Dividend_Yield() == 0:
            return 0.0
        return mark_safe(f"{obj.Dividend_Yield()}%")

    Dividend_Yield_.short_description = "Dividend Yield"

    def EBIT_ACTIVOS_(self, obj):
        if obj.EBIT_ACTIVOS() is None:
            return "Sem registo"
        if obj.EBIT_ACTIVOS() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"{obj.EBIT_ACTIVOS()}")

    EBIT_ACTIVOS_.short_description = "EBIT ACTIVOS"

    def P_ACTIVO_(self, obj):
        if obj.P_ACTIVO() is None:
            return "Sem registo"
        if obj.P_ACTIVO() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"MZN {obj.P_ACTIVO()}")

    P_ACTIVO_.short_description = "P ACTIVO"

    def P_EBITDA_(self, obj):
        if obj.P_EBITDA() is None:
            return "Sem registo"
        if obj.P_EBITDA() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"MZN {obj.P_EBITDA()}")

    P_EBITDA_.short_description = "P EBITDA"

    def P_EBIT_(self, obj):
        if obj.P_EBIT() is None:
            return "Sem registo"
        if obj.P_EBIT() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"MZN {obj.P_EBIT()}")

    P_EBIT_.short_description = "P EBIT"

    def P_VPA_(self, obj):
        if obj.P_VPA() is None:
            return "Sem registo"
        if obj.P_VPA() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"MZN {obj.P_VPA()}")

    P_VPA_.short_description = "P VPA"

    def P_L_(self, obj):
        if obj.P_L() is None:
            return "Sem registo"
        if obj.P_L() == 0:
            return "Impossivel de calcular"
        return mark_safe(f"MZN {obj.P_L()}")

    P_L_.short_description = "P L"

    def Capital_de_Giro_Liquido_(self, obj):
        if obj.Capital_de_Giro_Liquido() is None:
            return "Sem registo"
        if obj.Capital_de_Giro_Liquido() == 0:
            return obj.Capital_de_Giro_Liquido()
        return mark_safe(f"MZN {obj.Capital_de_Giro_Liquido()}")

    Capital_de_Giro_Liquido_.short_description = "Capital de Giro Liquido"

    def Capital_de_Giro_(self, obj):
        if obj.Capital_de_Giro() is None:
            return "Sem registo"
        if obj.Capital_de_Giro() == 0:
            return obj.Capital_de_Giro()
        return mark_safe(f"MZN {obj.Capital_de_Giro()}")

    Capital_de_Giro_.short_description = "Capital de Giro"

    def Vendas_Liquidas_(self, obj):
        if obj.Vendas_Liquidas() is None:
            return "Sem registo"
        if obj.Vendas_Liquidas() == 0:
            return obj.Vendas_Liquidas()
        return mark_safe(f"MZN {obj.Vendas_Liquidas()}")

    Vendas_Liquidas_.short_description = "Vendas Liquidas"

    def Activos_(self, obj):
        if obj.Activos() is None:
            return "Sem registo"
        if obj.Activos() == 0:
            return obj.Activos()
        return mark_safe(f"MZN {obj.Activos()}")

    Activos_.short_description = "Activos"

    def EBITDA_Func(self, obj):
        return obj.EBITDA_()

    EBITDA_Func.short_description = "EBITDA"

    def EBIT_Func(self, obj):
        if obj.EBIT_() is None:
            return "Sem registo"
        if obj.EBIT_() == 0:
            return obj.EBIT_()
        return mark_safe(f"MZN {obj.EBIT_()}")

    EBIT_Func.short_description = "EBIT"

    def VPL_(self, obj):
        if obj.VPL() is None:
            return "Sem registo"
        if obj.VPL() == 0:
            return obj.VPL()
        return mark_safe(f"MZN {obj.VPL()}")

    VPL_.short_description = "VPL"

    def LPA_(self, obj):
        if obj.LPA() is None:
            return "Sem registo"
        if obj.LPA() == 0:
            return obj.LPA()
        return mark_safe(f"MZN {obj.LPA()}")

    LPA_.short_description = "LPA"


@admin.register(IndicadoresDeEndividamento)
class IndicadoresDeEndividamentoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "Liquidez_Corrente_",
        "Liquidez_Seca_",
        "Liquidez_Geral_",
        "Divida_or_Activo_Total_",
        "Divida_Patrimonio_Liquido_",
        "Divida_Liquido_EBITD_",
        "Divida_Liquido_EBITDA_",
        "Divida_Liquido_Lucro_Liquido_",
        "Divida_Bruta_Lucro_Liquido_",
        "Passivo_Activo",
    ]
    list_filter = [
        "nome_da_empresa",
    ]

    def Passivo_Activo(self, obj):
        if obj.Passivo_Activo() is None:
            return "Sem registo"
        if obj.Passivo_Activo() == 0:
            return obj.Passivo_Activo()
        return mark_safe(f"MZN {obj.Passivo_Activo()}")

    Passivo_Activo.short_description = "Passivo_Activo"

    def Divida_Bruta_Lucro_Liquido_(self, obj):
        if obj.Divida_Bruta_Lucro_Liquido() is None:
            return "Sem registo"
        if obj.Divida_Bruta_Lucro_Liquido() == 0:
            return obj.Divida_Bruta_Lucro_Liquido()
        return mark_safe(f"MZN {obj.Divida_Bruta_Lucro_Liquido()}")

    Divida_Bruta_Lucro_Liquido_.short_description = "Divida Bruta/Lucro Liquido"

    def Divida_Liquido_Lucro_Liquido_(self, obj):
        if (
            obj.Divida_Liquido_Lucro_Liquido() is None
            or obj.Divida_Liquido_Lucro_Liquido() == 0
        ):
            return "Sem registo"
        return mark_safe(f"MZN {obj.Divida_Liquido_Lucro_Liquido()}")

    Divida_Liquido_Lucro_Liquido_.short_description = "Divida Líquida/Lucro Liquido"

    def Divida_Liquido_EBITDA_(self, obj):
        return obj.Divida_Liquido_EBITDA()

    Divida_Liquido_EBITDA_.short_description = "Divida Liquido EBITDA"

    def Divida_Liquido_EBITD_(self, obj):
        if obj.Divida_Liquido_EBITD() is None or obj.Divida_Liquido_EBITD() == 0:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Divida_Liquido_EBITD()}")

    Divida_Liquido_EBITD_.short_description = "Divida Liquido EBITD"

    def Divida_Patrimonio_Liquido_(self, obj):
        if (
            obj.Divida_Patrimonio_Liquido() is None
            or obj.Divida_Patrimonio_Liquido() == 0
        ):
            return "Sem registo"
        return mark_safe(f"MZN {obj.Divida_Patrimonio_Liquido()}")

    Divida_Patrimonio_Liquido_.short_description = "Divida Patrimonio Liquido"

    def Divida_or_Activo_Total_(self, obj):
        if obj.Divida_or_Activo_Total() is None:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Divida_or_Activo_Total()}")

    Divida_or_Activo_Total_.short_description = "Divida or Activo Total"

    def Liquidez_Geral_(self, obj):
        if obj.Liquidez_Geral() is None:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Liquidez_Geral()}")

    Liquidez_Geral_.short_description = "Liquidez Geral"

    def Liquidez_Seca_(self, obj):
        if obj.Liquidez_Seca() is None:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Liquidez_Seca()}")

    Liquidez_Seca_.short_description = "Liquidez Seca"

    def Liquidez_Corrente_(self, obj):
        if obj.Liquidez_Corrente() is None:
            return "Sem registo"
        return mark_safe(f"MZN {obj.Liquidez_Corrente()}")

    Liquidez_Corrente_.short_description = "Liquidez Corrente"


@admin.register(IndicadoresDeCrescimento)
class IndicadoresDeCrescimentoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "CAGR_Receita_5A_",
        "CAGR_Lucro_5A_",
    ]
    list_filter = [
        "nome_da_empresa",
    ]

    def CAGR_Receita_5A_(self, obj):
        if obj.CAGR_Receita_5A() is None:
            return mark_safe(f"Sem registo")
        return mark_safe(f"{obj.CAGR_Receita_5A()}%")

    CAGR_Receita_5A_.short_description = "CAGR Receita 5A"

    def CAGR_Lucro_5A_(self, obj):
        if obj.CAGR_Lucro_5A() is None:
            return mark_safe(f"Sem registo")
        return mark_safe(f"{obj.CAGR_Lucro_5A()}%")

    CAGR_Lucro_5A_.short_description = "CAGR Lucro 5A"


@admin.register(IndicadoresDeEficiencia)
class IndicadoresDeEficienciaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "margem_bruta_",
        "margin_EBITIDA_",
        "margin_EBIT_",
        "margin_Liquida_",
    ]
    list_filter = [
        "nome_da_empresa",
    ]

    def margem_bruta_(self, obj):
        if obj.margem_bruta() is None:
            return "Sem registo"
        return mark_safe(f"{obj.margem_bruta()}%")

    margem_bruta_.short_description = "Margem Bruta"

    def margin_EBITIDA_(self, obj):
        return obj.margin_EBITIDA()

    def margin_Liquida_(self, obj):
        if obj.margin_Liquida() is None:
            return "Sem registo"
        return mark_safe(f"{obj.margin_Liquida()}%")

    margin_Liquida_.short_description = "Margin Liquida"

    def margin_EBIT_(self, obj):
        if obj.margin_EBIT() is None:
            return "Sem registo"
        return mark_safe(f"{obj.margin_EBIT()}%")

    margin_EBIT_.short_description = "margin EBIT"


@admin.register(IndicadoresDeRentabilidade)
class IndicadoresDeRentabilidadeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "ROA",
        "ROE_",
        "Roic_",
        "Giro_dos_Activos",
    ]
    list_filter = ["nome_da_empresa"]

    # def ROA_(self, obj):
    #     if obj.ROA() is None:
    #         return "Sem registo"
    #     return mark_safe(f"{obj.ROA()}%")

    # ROA_.short_description = "ROA"

    def ROE_(self, obj):
        if obj.ROE() is None:
            return "Sem registo"
        return mark_safe(f"{obj.ROE()}%")

    ROE_.short_description = "ROE"

    def Roic_(self, obj):
        if obj.Roic() is None:
            return "Sem registo"
        return mark_safe(f"{obj.Roic()}%")

    Roic_.short_description = "Roic"

    # def Giro_dos_Activos(self, obj):
    #     if obj.Giro_dos_Activos() is None:
    #         return "Sem registo"
    #     return mark_safe(f"MZN {obj.Giro_dos_Activos()}")

    # Giro_dos_Activos.short_description = "Giro_dos_Activos"


@admin.register(DemonstracaoDeFluxoDeCaixa)
class DemonstracaoDeFluxoDeCaixaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "fundos_gerados_das_actividades_operacionais",
        "fundos_utilizados_em_actividades_de_investimento",
        "fundos_introduzidos_atraves_de_actividades_de_financiamento",
        "acrescimo_ou_decrescimo_em_caixa_e_equivalentes_de_caixa",
        "fluxo_de_caixa",
    ]

    def fluxo_de_caixa(self, obj):
        return obj.fluxo_de_caixa()

    fluxo_de_caixa.short_description = "Fluxo de Caixa"


@admin.register(DemonstracaoDeResultados)
class DemonstracaoDeResultadosAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "vendas",
        "lucros_bruto",
        "EBITIDA",
        "EBIT",
        "lucro_antes_de_imposto",
        "impostos",
        "lucro_liquido_depois_de_imposto",
        "dividendo_declarados_e_pagos",
        "numero_medio_ponderado_de_acoes",
        "lucro_por_acao",
        "dividendo_por_acao",
    ]
    list_filter = ["nome_da_empresa"]

    def impostos(self, obj):
        return obj.impostos()

    impostos.short_description = "Importos"

    def lucro_por_acao(self, obj):
        return obj.lucro_por_acao()

    lucro_por_acao.short_description = "Lucro por Acao"

    def dividendo_por_acao(self, obj):
        return obj.dividendo_por_acao()

    dividendo_por_acao.short_description = "Dividendo por Acao"


@admin.register(TableDeDivida)
class TableDeDividaAdmin(admin.ModelAdmin):
    list_display = ["id", "ano_", "nome_da_empresa", "divida_bruta", "divida_liquida"]
    # list_editable = ['nome_da_empresa']
    list_filter = ["nome_da_empresa"]

    def ano_(self, obj):
        return obj.ano

    ano_.short_description = "Ano"

    def divida_liquida(self, obj):
        return obj.divida_liquida()

    divida_liquida.short_description = "Divida Liquida"

    def balanco_(self, obj):
        return obj.balanco

    balanco_.short_description = "Divida Bruta"


@admin.register(Balanco)
class BalancoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "ano",
        "nome_da_empresa",
        "activo_corrente",
        "caixa",
        "inventarios",
        "activo_nao_corrente",
        "total_de_activo",
        "passivo_corrente",
        "passivo_nao_corrente",
        "total_de_passivo",
        "capital_social",
        "reservas_nao_distribuidas",
        # 'premio_de_emissao',
        # 'lucros_acumulados',
        # 'lucros_acumulados_2',
        # 'disconto_de_premio_das_acoes_proprias',
        "disconto_e_premio_das_acoes_proprias_",
        "resultados_transitado",
        "resultados_de_exercicio",
        "lucros_acumulados_geral",
        "total_do_capital_proprio",
        "total_do_passvo_e_capital_proprio",
        "additional_column1",
        "additional_column2",
        "additional_column3",
        "additional_column4",
    ]
    # list_editable = ['nome_da_empresa']
    list_filter = ["nome_da_empresa"]

    def lucros_acumulados_geral(self, obj):
        return obj.lucros_acumulados_geral()

    lucros_acumulados_geral.short_description = "Lucros Acumulados"

    def total_do_passvo_e_capital_proprio(self, obj):
        return obj.total_do_passvo_e_capital_proprio()

    total_do_passvo_e_capital_proprio.short_description = (
        "Total do Passvo e Capital Proprio"
    )

    def total_do_capital_proprio(self, obj):
        return obj.total_do_capital_proprio()

    total_do_capital_proprio.short_description = "Total do Capital Proprio"

    def total_de_passivo(self, obj):
        return obj.total_de_passivo()

    total_de_passivo.short_description = "Total do Passivo"

    def total_de_activo(self, obj):
        return obj.total_de_activo()

    total_de_activo.sort_description = "Total do Activo"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "location",
    ]
    list_display_links = ["id", "user"]

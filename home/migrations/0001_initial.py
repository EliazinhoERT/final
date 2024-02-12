# Generated by Django 5.0.1 on 2024-01-13 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="CDM", max_length=125, unique=True)),
                (
                    "sector_de_actuacao",
                    models.CharField(
                        choices=[
                            ("bebidas", "Bebidas"),
                            ("seguros", "Seguros"),
                            ("prestacao-de-servicos", "Prestação de Serviços"),
                            ("financeiro", "Financeiro"),
                            ("petroleo-e-gas", "Petróleo e Gás"),
                            ("comercio", "Comércio"),
                            ("energia-hidroelectrica", "Energia Hidroelectrica"),
                            ("portagem", "Portagem"),
                            ("marketing", "Marketing"),
                            ("industria", "industria"),
                            ("agricultura", "Agricultura"),
                            ("importacao-e-exportacao", "Importação e Exportação"),
                        ],
                        default="bebidas",
                        max_length=100,
                    ),
                ),
                (
                    "company_logo",
                    models.ImageField(
                        default="comany_logs/no_image.png", upload_to="comany_logs/"
                    ),
                ),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Balanco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "activo_corrente",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "caixa",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "inventarios",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "activo_nao_corrente",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "passivo_corrente",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "passivo_nao_corrente",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "capital_social",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "premio_de_emissao",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "reservas_nao_distribuidas",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "lucros_acumulados",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "disconto_de_premio_das_acoes_proprias",
                    models.DecimalField(decimal_places=2, default=-1.0, max_digits=20),
                ),
                (
                    "resultados_transitado",
                    models.DecimalField(decimal_places=2, default=-1.0, max_digits=20),
                ),
                (
                    "resultados_de_exercicio",
                    models.DecimalField(decimal_places=2, default=-1.0, max_digits=20),
                ),
                (
                    "additional_column1",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=20,
                        verbose_name="Columa Adicional 1",
                    ),
                ),
                (
                    "additional_column2",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=20,
                        verbose_name="Columa Adicional 2",
                    ),
                ),
                (
                    "additional_column3",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=20,
                        verbose_name="Columa Adicional 3",
                    ),
                ),
                (
                    "additional_column4",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=20,
                        verbose_name="Columa Adicional 4",
                    ),
                ),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Balanco",
                "verbose_name_plural": "Balancos",
            },
        ),
        migrations.CreateModel(
            name="CotacoesDasAcoes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(blank=True)),
                (
                    "preco_da_acao",
                    models.DecimalField(decimal_places=2, default=0, max_digits=20),
                ),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.company"
                    ),
                ),
            ],
            options={
                "verbose_name": "Cotacao Da Acao",
                "verbose_name_plural": "Cotacoes Das Acoes",
            },
        ),
        migrations.CreateModel(
            name="DemonstracaoDeFluxoDeCaixa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "fundos_gerados_das_actividades_operacionais",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "fundos_utilizados_em_actividades_de_investimento",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "fundos_introduzidos_atraves_de_actividades_de_financiamento",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "acrescimo_ou_decrescimo_em_caixa_e_equivalentes_de_caixa",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Demonstracao De Fluxos De Caixas",
            },
        ),
        migrations.CreateModel(
            name="DemonstracaoDeResultados",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "vendas",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=20
                    ),
                ),
                (
                    "lucros_bruto",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0.0, max_digits=20
                    ),
                ),
                (
                    "EBITIDA",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "EBIT",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "lucro_antes_de_imposto",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "lucro_liquido_depois_de_imposto",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "dividendo_declarados_e_pagos",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "numero_medio_ponderado_de_acoes",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Demonstracao De Resultados",
                "verbose_name_plural": "Demonstracao De Resultados",
            },
        ),
        migrations.CreateModel(
            name="IndicadoresDeCrescimento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "ordering": ("ano",),
            },
        ),
        migrations.CreateModel(
            name="IndicadoresDeEficiencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="IndicadoresDeEndividamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "ordering": ("ano",),
            },
        ),
        migrations.CreateModel(
            name="IndicadoresDeRentabilidade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="MetricasPorAccao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "ordering": ("-ano",),
            },
        ),
        migrations.CreateModel(
            name="TableDeDivida",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ano", models.CharField(blank=True, default="2015", max_length=50)),
                (
                    "divida_bruta",
                    models.DecimalField(blank=True, decimal_places=2, max_digits=20),
                ),
                (
                    "nome_da_empresa",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.company",
                    ),
                ),
            ],
            options={
                "verbose_name": "Table De Divida",
                "verbose_name_plural": "Table De Divida",
            },
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_member", models.BooleanField(default=False)),
                (
                    "location",
                    models.CharField(default="Cidade de Maputo", max_length=30),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
                "ordering": ("user",),
            },
        ),
    ]
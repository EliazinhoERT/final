# Generated by Django 5.0.1 on 2024-01-13 02:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_demonstracaoderesultados_ebit_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="demonstracaoderesultados",
            name="ano",
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="EBIT",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="EBITIDA",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="dividendo_declarados_e_pagos",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="lucro_antes_de_imposto",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="lucro_liquido_depois_de_imposto",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="lucros_bruto",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="numero_medio_ponderado_de_acoes",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="demonstracaoderesultados",
            name="vendas",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
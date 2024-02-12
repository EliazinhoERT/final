# Generated by Django 5.0.1 on 2024-01-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_noticias_sector_da_noticia"),
    ]

    operations = [
        migrations.AddField(
            model_name="cotacoesdasacoes",
            name="numero_de_accoes_negociadas",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="noticias",
            name="sector_da_noticia",
            field=models.CharField(
                choices=[
                    ("economia", "Economia"),
                    ("negocios", "Negócios"),
                    ("politica", "Política"),
                    ("tecnologias", "Tecnologias"),
                    ("petroleo-e-gas", "Petróleo e Gás"),
                    ("opiniao", "Opinião"),
                    ("datas-importantes", "Datas Importantes"),
                ],
                default="economia",
                max_length=100,
            ),
        ),
    ]

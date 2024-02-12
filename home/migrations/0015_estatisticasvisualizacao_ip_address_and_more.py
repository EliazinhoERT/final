# Generated by Django 5.0.2 on 2024-02-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_estatisticasvisualizacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='estatisticasvisualizacao',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AlterField(
            model_name='estatisticasvisualizacao',
            name='total_visualizacoes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

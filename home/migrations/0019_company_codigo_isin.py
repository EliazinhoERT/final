# Generated by Django 5.0.2 on 2024-02-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_company_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='codigo_isin',
            field=models.CharField(default='MZTRASAONEB1', max_length=200),
        ),
    ]

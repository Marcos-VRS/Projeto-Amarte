# Generated by Django 5.1 on 2024-09-09 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeiro", "0002_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="financeiro_cadastro",
            name="cpf_cnpj_numero",
            field=models.CharField(default="N/A", max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="financeiro_cadastro",
            name="cpf_cnpj_tipo",
            field=models.CharField(
                choices=[("CPF", "CPF"), ("CNPJ", "CNPJ")], default="CPF", max_length=4
            ),
        ),
    ]

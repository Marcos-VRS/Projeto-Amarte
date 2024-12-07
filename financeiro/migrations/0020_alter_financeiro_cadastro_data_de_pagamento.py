# Generated by Django 5.1 on 2024-10-08 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeiro", "0019_financeiro_cadastro_data_de_pagamento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="financeiro_cadastro",
            name="data_de_pagamento",
            field=models.CharField(
                max_length=2,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Deve conter apenas 2 números entre 01 e 31.",
                        regex="^([0-9]{1,2})$",
                    )
                ],
            ),
        ),
    ]
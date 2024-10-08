# Generated by Django 5.1 on 2024-10-08 14:48

import financeiro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("financeiro", "0022_alter_financeiro_cadastro_data_de_pagamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="financeiro_cadastro",
            name="data_de_pagamento",
            field=models.PositiveIntegerField(
                blank=True, null=True, validators=[financeiro.models.validate_day]
            ),
        ),
    ]

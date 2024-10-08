from django import forms
from .models import Financeiro_Cadastro, Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            "nome",
            "data",
            "hora",
            "duracao",
            "descricao",
            "recorrência",
            "repetições",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "data": forms.DateInput(
                format="%Y/%m/%d", attrs={"class": "form-control", "type": "date"}
            ),
            "hora": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "duracao": forms.TextInput(
                attrs={"placeholder": "Duração do evento (ex: 2 horas)"}
            ),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "recorrência": forms.Select(attrs={"class": "form-control"}),
            "repetições": forms.NumberInput(
                attrs={"class": "form-control", "min": "0"}
            ),
        }


class FinanceiroCadastroForm(forms.ModelForm):
    class Meta:
        model = Financeiro_Cadastro
        fields = [
            "nome",
            "telefone",
            "email",
            "descrição",
            "categoria",
            "cpf_cnpj_tipo",
            "cpf_cnpj_numero",
            "categoria_de_pagamento",
            "frequencia_de_pagamento",
            "data_de_pagamento",
            "valor_pago",  # Adicione o campo valor_pago
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "descrição": forms.Textarea(attrs={"class": "form-control"}),
            "categoria": forms.Select(
                attrs={"class": "form-control"}
            ),  # Lista de opções
            "cpf_cnpj_tipo": forms.Select(attrs={"class": "form-control"}),
            "cpf_cnpj_numero": forms.TextInput(attrs={"class": "form-control"}),
            "categoria_de_pagamento": forms.Select(attrs={"class": "form-control"}),
            "frequencia_de_pagamento": forms.Select(attrs={"class": "form-control"}),
            "data_de_pagamento": forms.TextInput(attrs={"class": "form-control"}),
            "valor_pago": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "0.00",  # Placeholder padrão
                    "step": "0.01",  # Incremento de casas decimais
                    "min": "0",  # Valor mínimo (pode ser ajustado)
                }
            ),  # Campo decimal personalizado
        }

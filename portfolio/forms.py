from django import forms
from .models import Projeto, Tecnologia


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = [
            'unidade_curricular',
            'titulo',
            'descricao',
            'conceitos_aplicados',
            'tecnologias',
            'competencias',
            'imagem',
            'video_demo',
            'github_link'
        ]

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = [
            'nome',
            'tipo',
            'descricao',
            'principais_aspetos',
            'nivel_interesse'
        ]
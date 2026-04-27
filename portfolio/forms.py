from django import forms
from .models import Projeto, Tecnologia,Competencia,Formacao


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

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = [
            'nome',
            'descricao',
            'nivel',
            'tipo',
        ]
        

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = [
            'titulo',
            'entidade',
            'tipo',
            'data_inicio',
            'data_fim',
            'descricao',
            'link_certificado',
            'tecnologias',
            'competencias',
        ]

from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
  class Meta:
    model = Projeto
    fields = ['unidade_curricular', 'titulo', 'descricao', 'conceitos_aplicados', 'tecnologias', 'competencias', 'imagem', 'video_demo', 'github_link']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['unidade_curricular'].required = True
        self.fields['titulo'].required = True
        self.fields['descricao'].required = True
        self.fields['conceitos_aplicados'].required = True
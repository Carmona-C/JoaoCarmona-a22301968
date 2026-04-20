from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, Competencia, TFC, Formacao, MakingOf


def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.prefetch_related('unidades_curriculares').all()
    return render(request, 'portfolio/licenciaturas.html', {'licenciaturas': licenciaturas})


def ucs_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes', 'projetos').all()
    return render(request, 'portfolio/ucs.html', {'ucs': ucs})


def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/projetos.html', {'projetos': projetos})


def tecnologias_view(request):
    tecnologias = Tecnologia.objects.prefetch_related('projetos', 'tfcs', 'formacoes').all()
    return render(request, 'portfolio/tecnologias.html', {'tecnologias': tecnologias})


def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('projetos', 'formacoes').all()
    return render(request, 'portfolio/competencias.html', {'competencias': competencias})


def tfcs_view(request):
    tfcs = TFC.objects.prefetch_related('tecnologias').all()
    return render(request, 'portfolio/tfcs.html', {'tfcs': tfcs})


def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'portfolio/formacoes.html', {'formacoes': formacoes})


def makingof_view(request):
    makingofs = MakingOf.objects.all()
    return render(request, 'portfolio/makingof.html', {'makingofs': makingofs})


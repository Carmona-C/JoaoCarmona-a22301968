from django.shortcuts import render
from .models import Licenciatura, UnidadeCurricular, Projeto, Tecnologia, Competencia, TFC, Formacao, MakingOf
from .forms import ProjetoForm
from .forms import TecnologiaForm
from .forms import CompetenciaForm
from .forms import FormacaoForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect


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

def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm()

    return render(request, 'criacao/novo_projeto.html', {'form': form})

def editar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)

        if form.is_valid():
            form.save()
            return redirect('projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'criacao/editar_projeto.html', {'form': form, 'projeto': projeto})


def apagar_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('projetos')


def nova_tecnologia_view(request):
    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm()

    return render(request, 'criacao/nova_tecnologia.html', {'form': form})

def editar_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)

    if request.method == 'POST':
        form = TecnologiaForm(request.POST, request.FILES, instance=tecnologia)

        if form.is_valid():
            form.save()
            return redirect('tecnologias')
    else:
        form = TecnologiaForm(instance=tecnologia)

    return render(request, 'criacao/editar_tecnologia.html', {'form': form, 'tecnologia': tecnologia})

def apagar_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect('tecnologias')


def nova_competencia_view(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm()

    return render(request, 'criacao/nova_competencia.html', {'form': form})

def editar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)

    if request.method == 'POST':
        form = CompetenciaForm(request.POST, request.FILES, instance=competencia)

        if form.is_valid():
            form.save()
            return redirect('competencias')
    else:
        form = CompetenciaForm(instance=competencia)

    return render(request, 'criacao/editar_competencia.html', {'form': form, 'competencia': competencia})

def apagar_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    competencia.delete()
    return redirect('competencias')


def nova_formacao_view(request):
    if request.method == 'POST':
        form = FormacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm()

    return render(request, 'criacao/nova_formacao.html', {'form': form})


def editar_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)

    if request.method == 'POST':
        form = FormacaoForm(request.POST, instance=formacao)
        if form.is_valid():
            form.save()
            return redirect('formacoes')
    else:
        form = FormacaoForm(instance=formacao)

    return render(request, 'criacao/editar_formacao.html', {'form': form, 'formacao': formacao})


def apagar_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    formacao.delete()
    return redirect('formacoes')
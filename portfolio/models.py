from django.db import models
from django import forms
# Create your models here.

class AreaCientifica(models.Model):
    nome_area = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField('Disciplina', related_name='areas_cientificas', blank=True)

    def __str__(self):
        return self.nome_area

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome_curso

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)  # Alterei para CharField para aceitar "1º Semestre"
    ects = models.IntegerField()
    curricularIUnitReadableCode = models.CharField(max_length=100)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome_disciplina

class Projeto(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_utilizadas = models.TextField()
    imagem = models.ImageField(upload_to='projeto_imagens', default='default_imagem.jpg')  # Defina o valor padrão para imagem
    video_demo_link = models.URLField(default='')
    github_link = models.URLField(default='')

    def __str__(self):
        return self.disciplina.nome_disciplina

class LinguagemProgramacao(models.Model):
    nome_linguagem = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_linguagem

class Docente(models.Model):
    nome_docente = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.disciplina:
            return f"{self.nome_docente} - ({self.disciplina.nome_disciplina})"
        else:
            return self.nome_docente
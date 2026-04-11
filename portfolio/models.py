from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField(blank=True)
    objetivos = models.TextField(blank=True)
    competencias = models.TextField(blank=True)
    duracao = models.IntegerField(default=3)
    ects = models.IntegerField(default=180)

    def __str__(self):
        return f"{self.nome} ({self.duracao} anos - {self.ects} ECTS)"


class Docente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    pagina_lusofona = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.email}" if self.email else self.nome


class UnidadeCurricular(models.Model):
    licenciatura = models.ForeignKey(Licenciatura,on_delete=models.CASCADE,related_name='unidades_curriculares',null=True,blank=True)
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=30,blank=True)
    ano = models.IntegerField(null=True,blank=True)
    semestre = models.CharField(max_length=20,blank=True)
    ects = models.IntegerField(null=True,blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='ucs',blank=True,null=True)
    docentes = models.ManyToManyField(Docente,related_name='unidades_curriculares',blank=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo}) - {self.ano}º ano" if self.codigo else f"{self.nome} - {self.ano}º ano"


class Tecnologia(models.Model):
    TIPO_CHOICES = [('linguagem','Linguagem'),('framework','Framework'),('bd','Base de Dados'),('ferramenta','Ferramenta'),('outra','Outra')]
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20,choices=TIPO_CHOICES,default='outra')
    descricao = models.TextField(blank=True)
    principais_aspetos = models.TextField(blank=True)
    nivel_interesse = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - Interesse {self.nivel_interesse}/5"


class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    nivel = models.IntegerField(default=3)
    tipo = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - Nível {self.nivel}/5" if self.tipo else f"{self.nome} - Nível {self.nivel}/5"


class Projeto(models.Model):
    unidade_curricular = models.ForeignKey(UnidadeCurricular,on_delete=models.CASCADE,related_name='projetos',null=True,blank=True)
    titulo = models.CharField(max_length=100,blank=True,default='')
    descricao = models.TextField(blank=True)
    conceitos_aplicados = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia,related_name='projetos',blank=True)
    competencias = models.ManyToManyField(Competencia,related_name='projetos',blank=True)
    imagem = models.ImageField(upload_to='projetos',blank=True,null=True)
    video_demo = models.URLField(blank=True)
    github_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.unidade_curricular.nome})" if self.unidade_curricular else self.titulo


class TFC(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100,blank=True)
    ano = models.IntegerField(null=True,blank=True)
    resumo = models.TextField(blank=True)
    area_cientifica = models.CharField(max_length=100,blank=True)
    interesse = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"


class Formacao(models.Model):
    titulo = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100,blank=True)
    tipo = models.CharField(max_length=50,blank=True)
    data_inicio = models.DateField(null=True,blank=True)
    data_fim = models.DateField(null=True,blank=True)
    descricao = models.TextField(blank=True)
    link_certificado = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia,related_name='formacoes',blank=True)
    competencias = models.ManyToManyField(Competencia,related_name='formacoes',blank=True)


    def __str__(self):
        return f"{self.titulo} - {self.entidade} ({self.tipo})" if self.tipo else f"{self.titulo} - {self.entidade}"


class MakingOf(models.Model):
    entidade = models.CharField(max_length=100,blank=True)
    titulo = models.CharField(max_length=100)
    trabalho_papel = models.ImageField(upload_to='makingof',blank=True,null=True)
    decisoes = models.TextField(blank=True)
    erros = models.TextField(blank=True)
    correcoes = models.TextField(blank=True)
    justificacao = models.TextField(blank=True)
    uso_ia = models.TextField(blank=True)

    
    def __str__(self):
        return f"{self.titulo} - Projeto: {self.projeto.titulo}" if self.projeto else (f"{self.titulo} - UC: {self.unidade_curricular.nome}" if self.unidade_curricular else f"{self.titulo} ({self.entidade})")
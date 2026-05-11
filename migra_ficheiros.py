import os
from django.core.files import File
from portfolio.models import UnidadeCurricular, Projeto, MakingOf


def migrar_ficheiro(objeto, nome_campo):
    ficheiro = getattr(objeto, nome_campo)

    if ficheiro and ficheiro.name:
        try:
            caminho_local = ficheiro.path
        except NotImplementedError:
            print(f"Já está na cloud: {objeto}")
            return

        if os.path.exists(caminho_local):
            with open(caminho_local, "rb") as f:
                ficheiro.save(
                    os.path.basename(caminho_local),
                    File(f),
                    save=True
                )

            print(f"Migrado: {objeto}")
        else:
            print(f"Não encontrado: {objeto} -> {caminho_local}")


for uc in UnidadeCurricular.objects.all():
    migrar_ficheiro(uc, "imagem")

for projeto in Projeto.objects.all():
    migrar_ficheiro(projeto, "imagem")

for makingof in MakingOf.objects.all():
    migrar_ficheiro(makingof, "trabalho_papel")
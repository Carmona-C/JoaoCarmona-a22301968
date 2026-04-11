import json
from django.core.management.base import BaseCommand
from portfolio.models import TFC, Tecnologia


class Command(BaseCommand):
    help = 'Importar TFCs a partir de JSON'

    def handle(self, *args, **kwargs):

        with open('portfolio/data/tfcs_deisi_2025.json', encoding='utf-8') as file:
            data = json.load(file)

        for item in data:

            tfc = TFC.objects.create(
                titulo=item.get('titulo',''),
                autor=item.get('autores',''),
                orientador=item.get('orientadores',''),
                licenciatura=item.get('licenciatura',''),
                resumo=item.get('resumo',''),
                palavras_chave=", ".join(item.get('palavras_chave', [])),
                area_cientifica=", ".join(item.get('areas', [])),
                pdf=item.get('pdf') or '',
                imagem=item.get('imagem') or '',
                email=item.get('email',''),
                interesse=item.get('rating',3)
            )

            # tecnologias
            for tech in item.get('tecnologias', []):
                tecnologia, created = Tecnologia.objects.get_or_create(
                    nome=tech
                )
                tfc.tecnologias.add(tecnologia)

        self.stdout.write(self.style.SUCCESS('TFCs importados com sucesso!'))
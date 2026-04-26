from django.urls import path
from . import views


urlpatterns = [
    path('', views.licenciaturas_view),  # homepage
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),

    path('projetos/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projetos/editar/<int:projeto_id>/', views.editar_projeto_view, name='editar_projeto'),
    path('projetos/apagar/<int:projeto_id>/', views.apagar_projeto_view, name='apagar_projeto'),

    path('tecnologias/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologias/editar/<int:tecnologia_id>/', views.editar_tecnologia_view, name='editar_tecnologia'),
    path('tecnologias/apagar/<int:tecnologia_id>/', views.apagar_tecnologia_view, name='apagar_tecnologia'),
]
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pessoa/', PessoaView.as_view(), name='pessoa'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('area_saber/', AreasDoSaberView.as_view(), name='area_saber'),
    path('curso/', CursoView.as_view(), name='curso'),
    path('turno/', TurnoView.as_view(), name='turno'),
    path('disciplina/', DisciplinaView.as_view(), name='disciplina'),
    path('matricula/', MatriculaView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacaoView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciaView.as_view(), name='frequencia'),
    path('turma/', TurmaView.as_view(), name='turma'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciaView.as_view(), name='ocorrencia'),
    path('disciplina_curso/', DisciplinaCursoView.as_view(), name='disciplina_curso'),
    path('tipo_avaliacao/', TipoAvaliacaoView.as_view(), name='tipo_avaliacao'),
]
from django.contrib import admin
from .models import *


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]


class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1
    fk_name = 'area_do_saber'

class AreasDoSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaInline]


class DisciplinaPorCursoInline(admin.TabularInline):
    model = DisciplinaPorCurso
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaPorCursoInline]


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

class CidadeAdmin(admin.ModelAdmin):
    list_filter = ['uf']

# Registro dos models com os novos admins
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(AreasDoSaber, AreasDoSaberAdmin)
admin.site.register(TipoAvaliacao)
admin.site.register(Turno)
admin.site.register(Turma)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(DisciplinaPorCurso)
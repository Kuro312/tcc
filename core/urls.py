from django.contrib import admin
from django.urls import path, include
from core.views import (
    core_home,
    core_turma_lista,
    core_gerenciar_turma,
    core_lista_dias,
    core_apagar_turma,
    core_aluno_home,
    core_gerenciar_dia,
    core_aluno_lista_turma,
    core_aluno_turma_gerenciar,
    core_aluno_dia_gerenciar,
    core_aluno_dia_arquivado_lista,
    core_aluno_dia_arquivado_gerenciar,
    core_turma_dia_gerenciar,
    core_turma_cadastrar,
    core_turma_dia_rota,
    core_aluno_atualizar,
    core_motorista_atualizar,
    core_aluno_rota,
)
urlpatterns = [
    # motorista

    path('motorista', core_home, name='core_home'),
    # lista das turmas
    path('motorista/turma', core_turma_lista, name='core_turma_lista'),


    # cadastrar turma
    path('motorista/turma/cadastrar', core_turma_cadastrar,
         name='core_turma_cadastrar'),

    # gerenciar uma turma especifica
    path('motorista/turma/gerenciar/<int:id>', core_gerenciar_turma,
         name='core_gerenciar_turma'),
    # lista dos dias
    path('motorista/turma/dia/lista/<int:id>',
         core_lista_dias, name='core_lista_dias'),
    # remover uma turma
    path('motorista/turma/remover/<int:id>',
         core_apagar_turma, name='core_apagar_turma'),

    # gerenciar um dia especifico
    path('motorista/turma/dia/<int:id>',
         core_gerenciar_dia, name='core_gerenciar_dia'),

    path('motorista/turma/dia/<int:idDia>/aluno/<int:idAluno>',
         core_turma_dia_gerenciar, name='core_turma_dia_gerenciar'),

    path('motorista/turma/dia/<int:idDia>/rota',
         core_turma_dia_rota, name='core_turma_dia_rota'),

    path('motorista/update/<int:id>', core_motorista_atualizar,
         name='core_motorista_atualizar'),




    # aluno
    # home do aluno
    path('aluno', core_aluno_home, name='core_aluno_home'),

    # lista de turmas as quais o aluno foi inserido
    path('aluno/turma/lista', core_aluno_lista_turma,
         name='core_aluno_lista_turma'),

    # gerenciamento de uma turma especifica
    path('aluno/turma/gerenciar/<int:idTurma>',
         core_aluno_turma_gerenciar, name='core_aluno_turma_gerenciar'),

    # gerenciamento de um dia especifico
    path('aluno/turma/dia/gerenciar/<int:idDia>',
         core_aluno_dia_gerenciar, name='core_aluno_dia_gerenciar'),
    # lista dos dias arquivados
    path('aluno/turma/diaArquivado/<int:idTurma>', core_aluno_dia_arquivado_lista,
         name='core_aluno_dia_arquivado_lista'),

    path('aluno/turmo/diaArquivado/gerenciar/<int:idDia>',
         core_aluno_dia_arquivado_gerenciar, name='core_aluno_dia_arquivado_gerenciar'),

    path('aluno/update/<int:id>', core_aluno_atualizar,
         name='core_aluno_atualizar'),


    path('aluno/dia/<int:idDia>/rota', core_aluno_rota, name='core_aluno_rota'),
]

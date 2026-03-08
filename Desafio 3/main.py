import csv
from aluno import Aluno
from disciplina import Disciplina
from curso import Curso
from nota import Nota
from gestor import GestorAcademico

gestor_academico = GestorAcademico()

gestor_academico.carregar_dados("Desafio 3/notas.csv")

gestor_academico.mostrar_alunos()
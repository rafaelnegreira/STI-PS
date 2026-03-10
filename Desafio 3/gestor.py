import csv
from aluno import Aluno
from disciplina import Disciplina
from curso import Curso
from nota import Nota

class GestorAcademico:
    def __init__(self):
        self.alunos = {}
        self.disciplinas = {}
        self.cursos = {}

    def carregar_dados(self, caminho_arquivo):
        try:
            with open(caminho_arquivo, mode='r') as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:

                    matricula = int(linha['MATRICULA'])
                    cod_disciplina = linha['COD_DISCIPLINA']
                    cod_curso = int(linha['COD_CURSO'])
                    nota_valor = int(linha['NOTA'])
                    carga_horaria = int(linha['CARGA_HORARIA'])
                    ano_semestre = int(linha['ANO_SEMESTRE'])
                
                    if cod_disciplina not in self.disciplinas:
                        self.disciplinas[cod_disciplina] = Disciplina(cod_disciplina, carga_horaria)
                    disciplina = self.disciplinas[cod_disciplina]

                    if matricula not in self.alunos:
                        self.alunos[matricula] = Aluno(matricula)
                    aluno = self.alunos[matricula]

                    if cod_curso not in self.cursos:
                        self.cursos[cod_curso] = Curso(cod_curso)
                    curso = self.cursos[cod_curso]

                    nova_nota = Nota(nota_valor, ano_semestre, cod_curso, disciplina)
                    aluno.notas.append(nova_nota)
                    disciplina.notas.append(nova_nota)

                    # Vincular Aluno ao Curso (Evitando duplicatas na lista do curso)
                    if aluno not in curso.alunos:
                        curso.alunos.append(aluno)
                        
            print("\nDados carregados!\n")

        except FileNotFoundError:
            print(f"Erro: Arquivo {caminho_arquivo} não encontrado")

    def mostrar_alunos(self):
        print(self.alunos.keys())
    
    def mostrar_cursos(self):
        print(self.cursos.keys())

    def mostrar_disciplinas(self):
        print(self.disciplinas.keys())

    def cr_alunos(self):
        print("\n     CR dos alunos\n")
        print("Matrícula        CR")
        for matricula in sorted(self.alunos):
            print(f"   {matricula}    -    {self.alunos[matricula].calcularCR()}")
    
    def media_cursos(self):
        print("\nMédia de CR dos cursos\n")
        print(" Curso         CR")
        for cod_curso in sorted(self.cursos):
            media = self.cursos[cod_curso].getMediaCR()
            print(f"   {cod_curso}    -    {media}") 
        
    def media_disciplinas(self):
        print("\n      Médias por Disciplina e Semestre\n")
        print(f"Disciplina     Semestre     Média")
        for cod in sorted(self.disciplinas.keys()):
            disciplina = self.disciplinas[cod]
            medias = disciplina.getMediaPorSemestre()
            
            if medias:
                for semestre in sorted(medias.keys()):
                    print(f" {cod}   |   {semestre}   |   {medias[semestre]}")
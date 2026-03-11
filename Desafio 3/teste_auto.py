import unittest
from aluno import Aluno
from disciplina import Disciplina
from nota import Nota
from curso import Curso

class TestAluno(unittest.TestCase):
    def teste_aluno_calcular_cr(self):

        aluno = Aluno(matricula=2026001)
        
        d1 = Disciplina("SEN00077", cargaHoraria=60)
        d2 = Disciplina("GCL00090", cargaHoraria=30)
        
        n1 = Nota(valor=0, anoSemestre=20181, codCurso=4, disciplina=d1)
        n2 = Nota(valor=72, anoSemestre=20182, codCurso=21, disciplina=d2)
        
        aluno.notas.append(n1)
        aluno.notas.append(n2)

        resultado_calculado = aluno.calcularCR()

        # Cáculo: ((0 * 60) + (72 * 30)) / (60 + 30)
        # (0 + 2160) / 90
        # 2160 / 90 = 24
        valor_esperado = 24
        
        self.assertEqual(resultado_calculado, valor_esperado)

    def teste_curso_getmediaCR(self):
        curso = Curso("Ciência da computação")

        #Primeiro aluno
        aluno = Aluno(matricula=2026001)
        
        d1 = Disciplina("SEN00077", cargaHoraria=60)
        d2 = Disciplina("GCL00090", cargaHoraria=30)
        
        n1 = Nota(valor=0, anoSemestre=20181, codCurso=4, disciplina=d1)
        n2 = Nota(valor=72, anoSemestre=20182, codCurso=4, disciplina=d2)
        
        aluno.notas.append(n1)
        aluno.notas.append(n2)

        curso.alunos.append(aluno)
        # Cáculo: ((0 * 60) + (72 * 30)) / (60 + 30)
        # (0 + 2160) / 90
        # 2160 / 90 = 24

        #Segundo aluno
        aluno = Aluno(matricula=2026002)
        
        d1 = Disciplina("SEN00030", cargaHoraria=60)
        d2 = Disciplina("GCL00100", cargaHoraria=60)
        
        n1 = Nota(valor=35, anoSemestre=20181, codCurso=4, disciplina=d1)
        n2 = Nota(valor=65, anoSemestre=20182, codCurso=4, disciplina=d2)
        
        aluno.notas.append(n1)
        aluno.notas.append(n2)

        curso.alunos.append(aluno)
        # Cáculo: ((35 * 60) + (65 * 60)) / (60 + 60)
        # (2100 + 3900) / 120
        # 6000 / 120 = 50

        valor_esperado = 37
        # Cálculo da média de CR do curso: (Aluno_1 + Aluno_2 + ... + Aluno_n) / n
        # (24 + 50) / 2 = 37

        self.assertEqual(valor_esperado, curso.getMediaCR())

if __name__ == '__main__':
    unittest.main()
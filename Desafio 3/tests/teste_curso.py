import unittest
from aluno import Aluno
from disciplina import Disciplina
from nota import Nota
from curso import Curso

class TestCurso(unittest.TestCase):
    def setUp(self):
        self.curso = Curso(21)
    
    def test_getmediaCR_vazio(self):
        """Testar o comportamento de um curso recém-criado"""
        self.assertEqual(self.curso.getMediaCR(), 0)
    
    def teste_curso_getmediaCR(self):
        """Verifica o comportamento do método getmediaCR"""
        #Primeiro aluno
        aluno = Aluno(matricula=2026001)
        
        d1 = Disciplina("SEN00077", cargaHoraria=60)
        d2 = Disciplina("GCL00090", cargaHoraria=30)
        
        n1 = Nota(valor=0, anoSemestre=20181, codCurso=21, disciplina=d1)
        n2 = Nota(valor=72, anoSemestre=20182, codCurso=21, disciplina=d2)
        
        aluno.notas.append(n1)
        aluno.notas.append(n2)

        self.curso.alunos.append(aluno)
        # Cáculo: ((0 * 60) + (72 * 30)) / (60 + 30)
        # (0 + 2160) / 90
        # 2160 / 90 = 24

        #Segundo aluno
        aluno = Aluno(matricula=2026002)
        
        d1 = Disciplina("SEN00030", cargaHoraria=60)
        d2 = Disciplina("GCL00100", cargaHoraria=60)
        
        n1 = Nota(valor=35, anoSemestre=20181, codCurso=21, disciplina=d1)
        n2 = Nota(valor=65, anoSemestre=20182, codCurso=21, disciplina=d2)
        
        aluno.notas.append(n1)
        aluno.notas.append(n2)

        self.curso.alunos.append(aluno)
        # Cáculo: ((35 * 60) + (65 * 60)) / (60 + 60)
        # (2100 + 3900) / 120
        # 6000 / 120 = 50

        valor_esperado = 37
        # Cálculo da média de CR do curso: (Aluno_1 + Aluno_2 + ... + Aluno_n) / n
        # (24 + 50) / 2 = 37

        resultado_calculado = self.curso.getMediaCR()

        self.assertEqual(valor_esperado, resultado_calculado)

if __name__ == '__main__':
    unittest.main()
import unittest
from aluno import Aluno
from disciplina import Disciplina
from nota import Nota

class TestAluno(unittest.TestCase):
    def setUp(self):
        self.aluno = Aluno(119174508)
    
    def test_cr_inicial_vazio(self):
        """Verifica o comportamento de um aluno recém-criado"""
        self.assertEqual(self.aluno.calcularCR(), 0)

    def teste_aluno_calcular_cr(self):
        """Verifica o comportamento do método calcular_cr"""
        # aluno = Aluno(matricula=2026001)
        
        d1 = Disciplina("SEN00077", cargaHoraria=60)
        d2 = Disciplina("GCL00090", cargaHoraria=30)
        
        n1 = Nota(valor=0, anoSemestre=20181, codCurso=4, disciplina=d1)
        n2 = Nota(valor=72, anoSemestre=20182, codCurso=21, disciplina=d2)
        
        self.aluno.notas.append(n1)
        self.aluno.notas.append(n2)

        resultado_calculado = self.aluno.calcularCR()

        # Cáculo: ((0 * 60) + (72 * 30)) / (60 + 30)
        # (0 + 2160) / 90
        # 2160 / 90 = 24
        valor_esperado = 24
        
        self.assertEqual(resultado_calculado, valor_esperado)

if __name__ == '__main__':
    unittest.main()
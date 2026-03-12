import unittest
from aluno import Aluno
from disciplina import Disciplina
from nota import Nota
from curso import Curso

class TestDisciplina(unittest.TestCase):

    def setUp(self):
        self.disciplina = Disciplina("GMA00019", 60)

    def test_media_semestre_unico(self):
        """Verifica se calcula a média para um semestre"""
        # Adicionamos duas notas no mesmo semestre
        n1 = Nota(100, 20171, 10, self.disciplina)
        n2 = Nota(80, 20171, 10, self.disciplina)
        
        self.disciplina.notas.extend([n1, n2])
        
        medias = self.disciplina.getMediaPorSemestre()
        
        # Esperado: (100 + 80) / 2 = 90.0
        self.assertEqual(medias[20171], 90.0)

    def test_multiplos_semestres(self):
        """Verifica se separa as médias por semestre"""
        # 20171: média 70 | 20172: média 90
        n1 = Nota(70, 20171, 10, self.disciplina)
        n2 = Nota(90, 20172, 10, self.disciplina)
        
        self.disciplina.notas.extend([n1, n2])
        
        medias = self.disciplina.getMediaPorSemestre()
        
        self.assertEqual(medias[20171], 70.0)
        self.assertEqual(medias[20172], 90.0)

    def test_disciplina_sem_notas(self):
        """Verifica quando não há notas cadastradas"""
        medias = self.disciplina.getMediaPorSemestre()
        
        # O resultado deve ser 0
        self.assertEqual(medias, 0)

if __name__ == '__main__':
    unittest.main()
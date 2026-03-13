import unittest

from gestor import GestorAcademico

class TestGestor(unittest.TestCase):

    def setUp(self):
        """Cria um arquivo CSV temporário para testar o carregamento"""
        self.caminho_csv = "notas.csv"
        self.gestor = GestorAcademico()
        self.gestor.carregar_dados(self.caminho_csv)

    def test_carregamento_unicidade_aluno(self):
        """Verifica se o gestor não cria alunos duplicados para a mesma matrícula"""
        
        # O dicionário de alunos deve ter 17 matrículas
        self.assertEqual(len(self.gestor.alunos), 17)

    def test_relacionamento_nota_aluno(self):
        """Verifica se as notas foram corretamente penduradas no objeto Aluno"""
        
        aluno = self.gestor.alunos[100]
        # O aluno 100 deve ter 16 objetos de Nota na sua lista
        self.assertEqual(len(aluno.notas), 16)

    def test_integridade_dos_dados(self):
        """Verifica se os valores convertidos do CSV estão corretos"""
        
        disciplina = self.gestor.disciplinas['MPS00012']
        # Verifica se a carga horária foi convertida para int corretamente
        self.assertEqual(disciplina.cargaHoraria, 30)

if __name__ == '__main__':
    unittest.main()
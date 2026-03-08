class Aluno:
    def __init__(self, matricula):
        self.matricula = matricula
        self.notas = []
        
    def calcularCR(self):
        return 10
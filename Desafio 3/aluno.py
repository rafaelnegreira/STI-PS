class Aluno:
    def __init__(self, matricula):
        self.matricula = matricula
        self.notas = []
        
    def calcularCR(self):
        numerador = 0
        denominador = 0

        for nota in self.notas:
            numerador = numerador + (nota.valor * nota.disciplina.cargaHoraria)
            denominador = denominador + (nota.disciplina.cargaHoraria)
        
        CR = numerador/denominador

        CR = round(CR, 2)

        return CR
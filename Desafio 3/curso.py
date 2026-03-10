class Curso:
    def __init__(self, codCurso):
        self.codCurso = codCurso
        self.alunos = []
        
    def getMediaCR(self):

        if not self.alunos: 
            return 0
        
        soma_cr = sum(aluno.calcularCR() for aluno in self.alunos)
        
        media = round(soma_cr / len(self.alunos), 2) 

        return media
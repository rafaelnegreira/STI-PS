class Disciplina:
    def __init__(self, codDisciplina, cargaHoraria):
        self.codDisciplina = codDisciplina
        self.cargaHoraria = cargaHoraria
        self.notas = []
        
    def getMediaPorSemestre(self):
        semestres = {}

        for nota in self.notas:
            if nota.anoSemestre not in semestres:
                semestres[nota.anoSemestre] = []
            semestres[nota.anoSemestre].append(nota.valor)

        medias = {}

        for ano_semestre, lista_notas in semestres.items():
            media = sum(lista_notas) / len(lista_notas)
            medias[ano_semestre] = round(media, 2)
        
        return medias
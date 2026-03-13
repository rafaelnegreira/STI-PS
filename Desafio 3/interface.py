from flask import Flask, render_template
from gestor import GestorAcademico

app = Flask(__name__)

# Instanciamos e carregamos os dados uma única vez ao iniciar o servidor
gestor = GestorAcademico()
gestor.carregar_dados("notas.csv")

@app.route('/')
def home():
    def pegar_matricula(aluno):
        return aluno.matricula
    
    def pegar_codCurso(curso):
        return curso.codCurso
    
    alunos_ordenados = sorted(gestor.alunos.values(), key=pegar_matricula)
    cursos_ordenados = sorted(gestor.cursos.values(), key=pegar_codCurso)
    
    return render_template('index.html', alunos=alunos_ordenados, cursos=cursos_ordenados)

# @app.route('/disciplinas')
# def disciplinas():
#     disciplinas_ordenadas = sorted(gestor.)
# if __name__ == '__main__':
#     app.run(debug=True)
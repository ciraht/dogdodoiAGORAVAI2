from flask import Flask, render_template, request, redirect

app = Flask(__name__)

consultas = []


# Código[0], nome[1], horario[2], data[3], nome do tutor[4], sintomas/motivo[5]

@app.route('/')
def index():
    return render_template('index.html', consultas=consultas)


@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        horario = request.form['horario']
        data = request.form['data']
        nometutor = request.form['nome-tutor']
        codigo = request.form['codigo']
        sintomas = request.form['sintomas']
        consultas.append([codigo, nomeanimal, horario, data, nometutor, sintomas])
        return redirect('/')
    else:
        return render_template('agendar_consulta.html')  # Renderiza o formulário de agendar consulta


if __name__ == '__main__':
    app.run(debug=True)

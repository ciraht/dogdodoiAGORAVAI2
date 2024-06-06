from flask import Flask, render_template, request, redirect

app = Flask(__name__)

pacientes = []


# Código[0], nome[1], espécie[2], raça[3], peso[4], nome do tutor[5]
# e telefone de contato [6].

@app.route('/')
def index():
    return render_template('index.html', pacientes=pacientes)


@app.route('/adicionar_paciente', methods=['GET', 'POST'])
def adicionar_paciente():
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nomeanimal, especie, raca, peso, nometutor, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_paciente.html')  # Renderiza o formulário de adicionar paciente


if __name__ == '__main__':
    app.run(debug=True)

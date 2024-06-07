from flask import Flask, render_template, request, redirect

app = Flask(__name__)
consultas = []
pacientes = []

@app.route('/')
def pagina_inicial():
    return render_template('index.html', pacientes=pacientes, consultas=consultas)

@app.route('/adicionar_paciente', methods=['GET', 'POST'])
def adicionar_paciente():
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        email = request.form['email']
        nometutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nomeanimal, especie, raca, peso, nometutor, email, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_paciente.html')


@app.route('/editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def editar_paciente(codigo):
    if request.method == 'POST':
        nomeanimal = request.form['nome']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nometutor = request.form['nome-tutor']
        email = request.form['email']
        telefone = request.form['telefone']

        pacientes[codigo] = [codigo, nomeanimal, especie, raca, peso, nometutor, email, telefone]

        return redirect('/')
    else:
        paciente = pacientes[codigo]
        return render_template('editar_paciente.html', paciente=paciente)




@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        nomeanimal = request.form['nomes']
        horario = request.form['horario']
        data = request.form['data']
        nometutor = request.form['nome-tutor']
        codigo = request.form['codigo']
        sintomas = request.form['sintomas']
        consultas.append([codigo, nomeanimal, horario, data, nometutor, sintomas])
        return redirect('/')
    else:
        return render_template('agendar_consulta.html', pacientes=pacientes)  # Renderiza o formulário de agendar consulta


@app.route('/calculadora_idade')
def index():
    return render_template("calculadora_idade.html", mensagem='')

@app.route('/calculadora_idade', methods=['POST'])
def calculadora_idade():
    ser = request.form.get('ser')
    idade = int(request.form.get('idade'))
    mensagem = ''

    if ser == "Cachorro":
        if idade == 1:
            mensagem = "1 ano para o cachorro equivalem a 15 anos para o ser humano"
        elif idade == 2:
            mensagem = "2 anos para o cachorro equivalem a 24 anos para o ser humano"
        elif idade == 3:
            mensagem = "3 anos para o cachorro equivalem a 28 anos para o ser humano"
        elif idade == 4:
            mensagem = "4 anos para o cachorro equivalem a 32 anos para o ser humano"
        elif idade == 5:
            mensagem = "5 anos para o cachorro equivalem a 36 anos para o ser humano"
        elif idade == 6:
            mensagem = "6 anos para o cachorro equivalem a 40 anos para o ser humano"
        elif idade >= 7:
            idade_equivalente = 44 + (idade - 7) * 5
            mensagem = f"{idade} anos para o cachorro equivalem a {idade_equivalente} anos para o ser humano"

    elif ser == "Gato":
        if idade == 1:
            mensagem = "1 ano para o gato equivalem a 15 anos para o ser humano"
        elif idade == 2:
            mensagem = "2 anos para o gato equivalem a 24 anos para o ser humano"
        elif idade == 3:
            mensagem = "3 anos para o gato equivalem a 28 anos para o ser humano"
        elif idade == 4:
            mensagem = "4 anos para o gato equivalem a 32 anos para o ser humano"
        elif idade == 5:
            mensagem = "5 anos para o gato equivalem a 36 anos para o ser humano"
        elif idade >= 6:
            idade_equivalente = 40 + (idade - 6) * 4
            mensagem = f"{idade} anos para o gato equivalem a {idade_equivalente} anos para o ser humano"

    else:
        mensagem = "Você escreveu algo errado! Confira de novo"

    return render_template('calculadora_idade.html', mensagem=mensagem)






@app.route('/medicamento', methods=['GET'])
def mostrar_formulario():
    return render_template('medicamento.html', volume_total='', dose='')
@app.route('/medicamento', methods=['POST'])
def calcular_soro():
    grau_desidratacao = request.form.get('grau_desidratacao')
    peso_animal = float(request.form.get('peso_animal'))

    if grau_desidratacao == 'Leve':
        volume_fluidoterapia = 50
    elif grau_desidratacao == 'Moderada':
        volume_fluidoterapia = 75
    elif grau_desidratacao == 'Grave':
        volume_fluidoterapia = 100
    else:
        volume_fluidoterapia = 0

    volume_total = volume_fluidoterapia * peso_animal

    return render_template('medicamento.html', volume_total=volume_total)


@app.route('/dose', methods=['POST'])
def medida_medicamento():
    medicamento = request.form.get('remedio')
    peso_animal2 = float(request.form.get('peso_animal2'))

    if medicamento == 'Petrilan':
        valor = 5
    elif medicamento == 'Canidexa':
        valor = 10
    elif medicamento == 'Felinoflam':
        valor = 3
    elif medicamento == 'Puprilon':
        valor = 7
    elif medicamento == 'Meowmed':
        valor = 4
    elif medicamento == 'Vetranix':
        valor = 6
    elif medicamento == 'Caniforte':
        valor = 8
    elif medicamento == 'FeliCure':
        valor = 5
    elif medicamento == 'Pawsitrex':
        valor = 4.5
    elif medicamento == 'WoofGuard':
        valor = 9
    elif medicamento == 'Outro':
        valor = float(request.form.get('outros'))
    else:
        return 'Medicamento inválido'

    dose = valor * peso_animal2

    return render_template('medicamento.html', dose=dose)





if __name__ == '__main__':
    app.run(debug=True)
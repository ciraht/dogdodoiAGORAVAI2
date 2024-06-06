from flask import Flask, render_template, request

app = Flask(__name__)


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

# @app.route('/medicamento')
# def mostrar_formulario():
#     return render_template('medicamento.html', volume_total='')

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
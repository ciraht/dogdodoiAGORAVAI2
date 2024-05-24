from flask import Flask, render_template, request

app = Flask(__name__)

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
        return 'Grau de desidratação inválido'

    volume_total = volume_fluidoterapia * peso_animal

    #return f'O volume total de soro necessário é: {volume_total} ml/kg'
    return render_template('medicamento.html', volume_total=volume_total)

@app.route('/medicamento')
def mostrar_formulario():
    return render_template('medicamento.html', volume_total='')

if __name__ == '__main__':
    app.run(debug=True)
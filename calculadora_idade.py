from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
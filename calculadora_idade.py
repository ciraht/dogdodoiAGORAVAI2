from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/calculadora_idade', methods=['GET'])
def mostrar_formulario():
    return render_template('calculadora_idade.html', anos='')

@app.route('/calculadora_idade', methods=['GET', 'POST'])
def calculadora_idade():
  ser = request.form.get('ser')
  acaba = 0

  if ser == "Cachorro":
    idade = request.form.get('idade')
    if idade == 1:
      return "1 ano para o cachorro equivalem a 15 anos para o ser humano"
    elif idade == 2:
      return "2 anos para o cachorro equivalem a 24 anos para o ser humano"
    elif idade == 3:
      return "3 anos para o cachorro equivalem a 28 anos para o ser humano"
    elif idade == 4:
      return "4 anos para o cachorro equivalem a 32 anos para o ser humano"
    elif idade == 5:
      return "5 anos para o cachorro equivalen a 36 anos para o ser humano"
    elif idade == 6:
      return "6 anos para o cachorro equivalen a 40 anos para o ser humano"
    elif idade == 7:
      return "7 anos para o cachorro equivalem a 44 anos para o ser humano"
    else:
      while True:
        conta = idade - 7
        anos = conta * 5
        return f"{idade} anos para o cachorro equivalem a {anos + 44} para o ser humano"
        acaba += 1
        if acaba == 1:
          break

  elif ser == "Gato":
    idade = request.form.get('idade')
    if idade == 1:
      return "1 ano para o gato equivalem a 15 anos para o ser humano"
    elif idade == 2:
      return "2 anos para o gato equivalem a 24 anos para o ser humano"
    elif idade == 3:
      return "3 anos para o gato equivalem a 28 anos para o ser humano"
    elif idade == 4:
      return "4 anos para o gato equivalem a 32 anos para o ser humano"
    elif idade == 5:
      return "5 anos para o gato equivalen a 36 anos para o ser humano"
    elif idade == 6:
      return"6 anos para o gato equivalen a 40 anos para o ser humano"
    else:
      while True:
        conta = idade - 6
        anos = conta * 4
        return f"{idade} anos para o cachorro equivalem a {anos + 40} para o ser humano"
        acaba += 1
        if acaba == 1:
          break

  else:
    return "Você escreveu algo errado! confira de novo"


  return render_template("calculadora_idade.html", anos=anos)



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import math

app = Flask(__name__)


@app.route('/calcular', methods=['GET'])
def calcular():
    numero = request.args.get('numero')
    operacao = request.args.get('operacao')

    if numero is None:
        return jsonify({
            "erro": "O parâmetro 'numero' é obrigatório."
        }), 400

    if operacao is None:
        return jsonify({
            "erro": "O parâmetro 'operacao' é obrigatório."
        }), 400

    try:
        numero = float(numero)
    except ValueError:
        return jsonify({
            "erro": "O parâmetro 'numero' deve ser numérico."
        }), 400

    operacoes_permitidas = ["quadrado", "cubo", "raiz"]

    if operacao not in operacoes_permitidas:
        return jsonify({
            "erro": "Operação inválida. Use: quadrado, cubo ou raiz."
        }), 400

    if operacao == "quadrado":
        resultado = numero ** 2

    elif operacao == "cubo":
        resultado = numero ** 3

    elif operacao == "raiz":
        if numero < 0:
            return jsonify({
                "erro": "Não é possível calcular a raiz de um número negativo."
            }), 400

        resultado = math.sqrt(numero)

    return jsonify({
        "numero": numero,
        "operacao": operacao,
        "resultado": resultado
    })

app.run(debug=True)
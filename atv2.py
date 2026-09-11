from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/saudacao/<nome>', methods=['GET'])
def saudacao(nome):
    return jsonify({
        "mensagem": f"Olá, {nome}!"
    })


app.run(debug=True)
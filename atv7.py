from flask import Flask, jsonify, request

app = Flask(__name__)


pessoas = [
    {
        "id": 1,
        "nome": "Vitoria",
        "idade": 15
    },
    {
        "id": 2,
        "nome": "Felipe",
        "idade": 16
    },
    {
        "id": 3,
        "nome": "Alberto",
        "idade": 99
    },
    {
        "id": 4,
        "nome": "Mantovani",
        "idade": 67
    }
]


@app.route('/busca', methods=['GET'])
def busca():
    nome = request.args.get('nome', '')
    idade_min = request.args.get('idade_min', '')
    idade_max = request.args.get('idade_max', '')

    resultado = pessoas

    if nome:
        resultado = [
            pessoa for pessoa in resultado
            if nome.lower() in pessoa["nome"].lower()
        ]

    if idade_min:
        resultado = [
            pessoa for pessoa in resultado
            if pessoa["idade"] >= int(idade_min)
        ]

    if idade_max:
        resultado = [
            pessoa for pessoa in resultado
            if pessoa["idade"] <= int(idade_max)
        ]

    return jsonify(resultado)


app.run(debug=True)
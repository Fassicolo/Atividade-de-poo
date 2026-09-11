from flask import Flask, jsonify, request

app = Flask(__name__)


produtos = [
    {
        "id": 1,
        "nome": "Notebook",
        "categoria": "eletronicos",
        "preco": 10000
    },
    {
        "id": 2,
        "nome": "Celular",
        "categoria": "eletronicos",
        "preco": 5000
    },
    {
        "id": 3,
        "nome": "Camiseta",
        "categoria": "roupas",
        "preco": 1000
    },
    {
        "id": 4,
        "nome": "Calça",
        "categoria": "roupas",
        "preco": 1500
    }
]


@app.route('/produtos', methods=['GET'])
def listar_produtos():
    categoria = request.args.get('categoria')

    if categoria:
        produtos_filtrados = [
            produto for produto in produtos
            if produto["categoria"].lower() == categoria.lower()
        ]
    else:
        produtos_filtrados = produtos

    return jsonify(produtos_filtrados)

app.run(debug=True)
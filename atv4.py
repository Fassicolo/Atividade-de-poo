from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/usuario', methods=['GET'])
def usuario():
    usuario = {
        "id": 1,
        "nome": "Vitoria",
        "idade": 15
    }

    return jsonify(usuario)


app.run(debug=True)
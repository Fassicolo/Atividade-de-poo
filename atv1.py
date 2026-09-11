from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ola', methods=['GET'])
def ola():
    return jsonify({
        "mensagem": "Hello, World!"
    })

app.run(debug=True)
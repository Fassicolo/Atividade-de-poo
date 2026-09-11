from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/soma', methods=['GET'])
def soma():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    resultado = a + b

    return jsonify({
        "resultado": resultado
    })


app.run(debug=True)
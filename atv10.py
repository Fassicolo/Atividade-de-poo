from flask import Flask, jsonify
import time
import random

app = Flask(__name__)


cache = {}

TEMPO_CACHE = 60


@app.route('/clima/<cidade>', methods=['GET'])
def clima(cidade):

    cidade = cidade.lower()

    tempo_atual = time.time()

    if cidade in cache:

        dados = cache[cidade]

        if tempo_atual - dados["tempo"] < TEMPO_CACHE:

            return jsonify({
                "cidade": cidade.title(),
                "temperatura": dados["temperatura"],
                "condicao": dados["condicao"],
                "cache": True
            })

    temperatura = random.randint(15, 35)

    condicoes = [
        "Ensolarado",
        "Nublado",
        "Chuvoso"
    ]

    condicao = random.choice(condicoes)

    cache[cidade] = {
        "temperatura": temperatura,
        "condicao": condicao,
        "tempo": tempo_atual
    }

    return jsonify({
        "cidade": cidade.title(),
        "temperatura": temperatura,
        "condicao": condicao,
        "cache": False
    })


app.run(debug=True)
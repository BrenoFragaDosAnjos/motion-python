
import tokeniza as tk

import operadores as op

from flask import Flask, request, jsonify


app = Flask(__name__)

# Rota para o endpoint de inserção de frase
@app.route('/inserir-frase', methods=['POST'])
def inserir_frase():
    frase = request.form.get('frase')

    # Verificar se a frase foi fornecida
    if not frase:
        return jsonify({'error': 'Frase não fornecida'}), 400

    lista_tokens = tk.tokeniza(frase)
    for token in lista_tokens:
        item, tipo = token
        if tipo == tk.PALAVRAS_NEGATIVAS:
                descricao = "'%s' : Frase negativa" %item
                tk.insertNegativa(frase)
        else:
                descricao = "'%s' : Palavras positivas" %item
                tk.insertPositiva(frase)       

    return jsonify({'message': 'Frase inserida com sucesso!'})

if __name__ == '__main__':
    app.run()



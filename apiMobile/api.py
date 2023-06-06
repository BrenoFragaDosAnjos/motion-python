from flask import Flask, request, jsonify
import connectDB as db
import json

app = Flask(__name__)

@app.route('/umidade',methods=['GET'])
def obterUmidade():
    try:
        sensores = db.recuperarUmidade()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500


@app.route('/vibracao',methods=['GET'])
def obterVibracao():
    try:
        sensores = db.recuperarVibracao()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500


@app.route('/ruido',methods=['GET'])
def obterRuido():
    try:
        sensores = db.recuperarRuido()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500


@app.route('/proximidade',methods=['GET'])
def obterProximidade():
    try:
        sensores = db.recuperarProximidade()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500


@app.route('/peso',methods=['GET'])
def obterPeso():
    try:
        sensores = db.recuperarPeso()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500


@app.route('/temperatura',methods=['GET'])
def obterTemperatura():
    try:
        sensores = db.recuperarTemperatura()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500

@app.route('/all',methods=['GET'])
def obterTodos():
    try:
        sensores = db.recuperarAll()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000,host= '0.0.0.0',debug=True)



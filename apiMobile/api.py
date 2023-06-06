from flask import Flask, request, jsonify
import connectDB as db
import json

app = Flask(__name__)

@app.route('/all',methods=['GET'])
def obterTodos():
    try:
        sensores = db.recuperarAll()
        return jsonify(sensores)
    except Exception as e:
        return jsonify({'success':False,'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000,host= '0.0.0.0',debug=True)



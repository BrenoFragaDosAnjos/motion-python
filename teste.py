import pyodbc
from flask import Flask, jsonify

app = Flask(__name__)

class Sensor:
    def __init__(self, nome, valor, data_captura):
        self.nome = nome
        self.valor = valor
        self.data_captura = data_captura

    def to_dict(self):
        return {
            'nome': self.nome,
            'valor': self.valor,
            'data_captura': self.data_captura.strftime('%Y-%m-%d %H:%M:%S')
        }

def recuperarSensor():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT * FROM SensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())  # Convertendo para dicionário

    response = {"success": True, "data": sensores}
    return response

@app.route('/sensores', methods=['GET'])
def obterSensores():
    response = recuperarSensor()
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
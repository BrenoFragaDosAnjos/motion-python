import pyodbc
from datetime import datetime, timedelta
import random

def gerar_dados():
    sensor_name = 'umidade'
    sensor_value_min = 50.0
    sensor_value_max = 80.0
    capture_date = datetime.now()

    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    cursor = conn.cursor()

    # Loop para inserir os dados
    for _ in range(300):
       
        sensor_value = random.uniform(sensor_value_min, sensor_value_max)
        formatted_date = capture_date.strftime('%Y-%m-%d %H:%M:%S')
        query = f"INSERT INTO SensorData (SensorName, SensorValue, CaptureDate) VALUES ('{sensor_name}', {sensor_value}, '{formatted_date}')"

        # Execução da query
        cursor.execute(query)
        conn.commit()
        capture_date += timedelta(hours=1)

    # Fechamento da conexão com o banco de dados
    cursor.close()
    conn.close()


gerar_dados()
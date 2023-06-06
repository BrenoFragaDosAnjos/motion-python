import pyodbc
import Sensor as sen


def recuperarAll():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "select id_viagem, temperatura, umidade, vibracao, ruido, proximidade, peso, latitude, longitude, data_captura from [dbo].[sensoresIntegrados]"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            id_viagem = row[0]
            temperatura = row[1]
            umidade = row[2]
            vibracao = row[3]
            ruido = row[4]
            proximidade = row[5]
            peso = row[6]
            latitude = row[7]
            longitude = row[8]
            data_captura = row[9]
           
            

            sensor = sen.Sensor(id_viagem,temperatura,umidade,vibracao,ruido,proximidade,peso,latitude,longitude,data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response


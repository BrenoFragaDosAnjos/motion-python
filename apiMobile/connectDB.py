import pyodbc
import Sensor as sen

def recuperarUmidade():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT * FROM SensorData"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarTemperatura():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'temperatura'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarVibracao():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'vibracao'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarRuido():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'ruido'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarProximidade():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'proximidade'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarPeso():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'peso'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarTemperatura():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData] WHERE SensorName = 'temperatura'"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

def recuperarAll():
    sensores = []
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "SELECT *FROM [dbo].[SensorData]"
    cursor.execute(sql)
    rows = cursor.fetchall()  # Chamada corrigida

    if len(rows) == 0:
        return {"success": True, "data": ""}

    else:
        for row in rows:
        # Extrair os valores das colunas
            nome = row[1]
            valor = row[2]
            data_captura = row[3]

            sensor = sen.Sensor(nome, valor, data_captura)
            sensores.append(sensor.to_dict())

    response = {"success": True, "data": sensores}
    print(sensores)
    conn.close()
    return response

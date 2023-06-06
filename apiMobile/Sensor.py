class Sensor:
    def __init__(self,id_viagem,temperatura,umidade,vibracao,ruido,proximidade,peso,latitude,longitude,data_captura):
        self.id_viagem = id_viagem
        self.temperatura = temperatura
        self.umidade = umidade
        self.vibracao = vibracao
        self.ruido = ruido
        self.proximidade = proximidade
        self.peso = peso
        self.latitude = latitude
        self.longitude = longitude
        self.data_captura = data_captura
        pass

    def to_dict(self):
        return {
            'id_viagem': self.id_viagem,
            'temperatura': self.temperatura,
            'umidade': self.umidade,
            'vibracao' : self.vibracao,
            'ruido' : self.ruido,
            'proximidade' : self.proximidade,
            'peso' : self.peso,
            'latitude' : self.latitude,
            'longitude' : self.longitude,
            'data_captura': self.data_captura.strftime('%Y-%m-%d %H:%M:%S')
        }


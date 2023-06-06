class Sensor:
    def __init__(self,nome,valor,data_captura):
        self.nome = nome
        self.valor = valor
        self.data_captura = data_captura
        pass

    def to_dict(self):
        return {
            'nome': self.nome,
            'valor': self.valor,
            'data_captura': self.data_captura.strftime('%Y-%m-%d %H:%M:%S')
        }


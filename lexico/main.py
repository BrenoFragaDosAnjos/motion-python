import esqueleto_tokeniza as tk
import operadores as op

PROMPT = "expressão >>> "
QUIT = ''

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

def main():
    print("Entre com uma expressão ou tecle apenas ENTER para encerrar.")
    expressao = input(PROMPT)
    
    while expressao != QUIT:
        lista_tokens = tk.tokeniza(expressao)
        
        for token in lista_tokens:
            tipo = token.tipo
            valor = token.valor

            if tipo in [tk.OPE1RADOR, tk.PARENTESES]:
                descricao = "'%s' : %s" % (valor, op.DESCRICAO[valor])
            elif tipo == tk.VARIAVEL:
                descricao = "'%s' : nome de variável" % valor
            elif tipo == tk.NUMERO:
                descricao = "%f : constante float" % valor
            else:
                descricao = "'%s' : categoria desconhecida" % valor

            print(descricao)

        expressao = input(PROMPT)

if __name__ == "__main__":
    main()
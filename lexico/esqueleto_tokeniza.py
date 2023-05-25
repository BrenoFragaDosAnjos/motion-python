import re

# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = OPERADORES # para operadores aritméticos e atribuição
NUMERO     = FLOATS # para números: todos são considerados float
VARIAVEL   = LETRAS # para variáveis
PARENTESES = ABRE_FECHA_PARENTESES# para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    
def tokeniza(exp) -> list:
    tokens = []
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            # Lidar com números
            numero = ""
            while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
                numero += exp[i]
                i += 1

            tokens.append(Token("NUMERO", float(numero)))

        elif exp[i] in "+-*/":
            # Lidar com operadores
            tokens.append(Token("OPERADOR", exp[i]))
            i += 1

        elif exp[i] == "(":
            # Lidar com parênteses de abertura
            tokens.append(Token("PARENTESES_ABERTO", exp[i]))
            i += 1

        elif exp[i] == ")":
            # Lidar com parênteses de fechamento
            tokens.append(Token("PARENTESES_FECHADO", exp[i]))
            i += 1

        else:
            # Lidar com outros caracteres desconhecidos
            i += 1

    return tokens
    



    

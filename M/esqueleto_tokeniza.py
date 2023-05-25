# Constantes
TESTE = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR = 1  # para operadores aritméticos e atribuição
NUMERO = 2  # para números: todos são considerados float
VARIAVEL = 3  # para variáveis
PARENTESES = 4  # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A função ignora tudo que está em `exp` após o caractere
    COMENTARIO (= "#").
    """
    tokens = []  # lista para armazenar os tokens

    # Remover comentários
    if COMENTARIO in exp:
        exp = exp[:exp.index(COMENTARIO)]

    i = 0  # índice para percorrer a expressão

    while i < len(exp):
        char = exp[i]

        # Verificar se é um operador
        if char in OPERADORES:
            tokens.append([char, OPERADOR])
            i += 1

        # Verificar se é um número
        elif char in FLOATS:
            start = i
            while i < len(exp) and exp[i] in FLOATS:
                i += 1
            num_str = exp[start:i]
            try:
                num = float(num_str)
                tokens.append([num, NUMERO])
            except ValueError:
                print(f"Erro: número inválido '{num_str}'")
                return []

        # Verificar se é uma variável
        elif char in LETRAS:
            start = i
            while i < len(exp) and exp[i] in LETRAS + DIGITOS:
                i += 1
            var = exp[start:i]
            tokens.append([var, VARIAVEL])

        elif char in BRANCOS:
            i += 1
        else:
            print(f"Erro: caractere desconhecido '{char}'")
            return []

    return tokens

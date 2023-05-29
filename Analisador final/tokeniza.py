import re
from better_profanity import profanity
import pyodbc
from googletrans import Translator

TESTE = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal 
PONTO = "."

# todos os caracteres usados em números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parênteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR = 1  # para operadores aritméticos e atribuição
NUMERO = 2  # para números: todos são considerados floatw
VARIAVEL = 3  # para variáveis
PARENTESES = 4  # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"

# palavras negativas
PALAVRAS_NEGATIVAS = True
PALAVRAS_POSITIVAS = False




#------------------------------------------------------------


def traduzir(texto):
    translator = Translator()
    traducao = translator.translate(texto, dest='en')
    return traducao.text

def insertPositiva(frase):
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "INSERT INTO FrasesPositivas (frase, data_captura) VALUES (?, GETDATE())"
    values = (frase,)
    cursor.execute(sql, values)
    conn.commit()
    print("Frase inserida com sucesso!")
    conn.close()

def insertNegativa(frase):
    conn = pyodbc.connect('Driver={ODBC Driver 18 for SQL Server};Server=tcp:wordserver.database.windows.net,1433;Database=word-database;Uid=urubu100;Pwd=14052002Kb4_;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = conn.cursor()
    sql = "INSERT INTO FrasesNegativas (frase, data_captura) VALUES (?, GETDATE())"
    values = (frase,)
    cursor.execute(sql, values)
    conn.commit()
    print("Frase inserida com sucesso!")
    conn.close()


def tokeniza(frase):   
    if COMENTARIO in frase:
        frase = frase.split(COMENTARIO, 1)[0]

    tokens = []
    if profanity.contains_profanity(traduzir(frase)) == True:
        tokens.append([frase, PALAVRAS_NEGATIVAS])
        
    else:
        tokens.append([frase, PALAVRAS_POSITIVAS])

    return tokens
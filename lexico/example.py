import profanity_check
import re

def censor_profanity(text):
    censor_text = text
    words = text.split()

    for i in range(len(words)):
        if profanity_check.predict([words[i]])[0] == 1:
            words[i] = re.sub(r'\w', '*', words[i])

    censor_text = ' '.join(words)
    return censor_text

# Exemplo de uso
text = input("Digite uma frase: ")

censored_text = censor_profanity(text)
print("Frase censurada: ", censored_text)
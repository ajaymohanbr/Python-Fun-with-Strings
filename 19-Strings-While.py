
# frase = 'O rato roeu a roupa do rei de roma'
#
# tamanho_frase = len(frase)  # 34 characters
#
# new = ''
# contador = 0

# while contador < tamanho_frase:
#     new += frase[contador]  # concatenation: All the characters copied to a new variable(new).
#     contador += 1
#
# print(new)

#
phrase = 'where there is a will, there is a way'
size = len(phrase)
letter = input('Which letter you´d like to see in uppercase? ')

i = 0
new = ''

while i < size:
    if phrase[i] == letter:
        new += phrase[i].upper()
    else:
        new += phrase[i]

    i += 1
print(new)


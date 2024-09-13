#Microatividade 5: Descrever a
#escrita de dados em um arquivo
#externo em Python

with open('texto.txt', 'w', encoding = 'utf-8') as file:
    texto = list()

    texto.append("1- Meu nome é Rodrigo de Paula.")
    texto.append("2- Tenho 38 anos, sou do RJ, gosto de rock e amo animais.")
    texto.append("3- Meu sonho, é me tornar um grande programador.")

    for linha in texto:
        file.write(linha + '\n')

print("O arquivo 'texto.txt' foi criado e escrito com sucesso.")

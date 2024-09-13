# Microatividade 4: Descrever a leitura
# de dados a partir de um arquivo
# externo em Python

with open('loremipsum.txt', 'r', encoding='utf-8') as file:
    content = file.read()


print(f"\nConteúdo completo do arquivo: \n{content}")
print()

primeira_linha = content.split('\n')[0]
print(f"\nPrimeira linha do arquivo: \n{primeira_linha}")
print()

tres_primeiras_letras = content[:3]
print(f"\nAs três primeiras letras do arquivo: \n{tres_primeiras_letras}")
print()

with open('loremipsum.txt', 'r', encoding='utf-8') as file:
    conteudo_with = file.read()

print(f"\nUtilizando o 'with' para ler o arquivo: \n{conteudo_with}")

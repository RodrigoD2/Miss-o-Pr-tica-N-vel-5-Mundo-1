# Microatividade 1: Descrever a
# ordenação de um array
# utilizando Python

array_numeros = [30, 21, 45, 89, 95, 58, 74, 68, 17, 22, 85, 7, 35, 91, 77]
print(f"\nExemplo de array com números: \n{array_numeros}")

array_numeros.sort()
print(f"\nNúmeros do array em ordem crescente: \n{array_numeros}")

array_numeros.sort(reverse=True)
print(f"\nNúmeros do array em ordem decrescente: \n{array_numeros}")

array_strings = ["nome", "dataNascimento", "cpf", "rg"]
print(f"\nExemplo de array com strings: \n{array_strings}")

array_strings.sort()
print(f"\nStrings do array em ordem crescente: \n{array_strings}")

array_strings.sort(reverse=True)
print(f"\nStrings do array em ordem decrescente: \n{array_strings}")

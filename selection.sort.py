# Microatividade 3: Descrevera utilização
# do algoritmo de ordenação “Selection Sort”
# em Python

def selectionSort(array):
    for i in range(len(array)):
        menor_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[menor_index]:
                menor_index = j
        if menor_index != i:
            array[i], array[menor_index] = array[menor_index], array[i]


array_numeros = [55, 38, 10, 91, 47, 82, 64, 22, 71, 16, 5, 39, 58, 19, 87]
print(f"Números do array fora de ordem:\n{array_numeros}")
selectionSort(array_numeros)
print(f"\nNúmeros do array em ordem:\n{array_numeros}")

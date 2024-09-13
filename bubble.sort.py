# Microatividade 2: Descrever a
# utilização do algoritmo de
# ordenação “Buble Sort” em Python

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


array_numeros = [15, 4, 8, 13, 7, 3, 10, 2, 9, 1, 12, 6, 11, 14, 5]
print(f"\nNúmeros do array \n{array_numeros}")
bubbleSort(array_numeros)
print(f"\nNúmeros do array de forma ordenada: \n{array_numeros}")

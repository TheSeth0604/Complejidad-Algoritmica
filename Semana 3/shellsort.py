import random

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr

arreglo = [random.randint(1, 10000) for i in range(1000)]

print("El arreglo generado es: ", arreglo)
print("El arreglo ordenado es: ", shell_sort(arreglo))
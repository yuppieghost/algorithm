def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high],arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr= [1, 3, 5, 5, 2, 9, 4]

quickSort(arr, 0, 6)
print(arr)

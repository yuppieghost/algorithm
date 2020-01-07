def partition(arr, low, high):
    pivot = arr[high]
    i = 0
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low >= high:
        return
    pi = partition(arr, low, high)
    quickSort(arr, 0, pi - 1)
    quickSort(arr, pi + 1, high)

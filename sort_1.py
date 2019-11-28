def bubble(l: list):
    n = len(l)

    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = True
        if not flag:
            break
    return l


assert bubble([9, 2, 5, 5, 2, 32, 8]) == [2, 2, 5, 5, 8, 9, 32]


def insert(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and k < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k
    return arr


assert insert([9, 2, 5, 5, 2, 32, 8]) == [2, 2, 5, 5, 8, 9, 32]


def select(arr):
    for i in range(len(arr)):
        minid = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minid]:
                minid = j
        arr[i], arr[minid] = arr[minid], arr[i]
    return arr


assert select([9, 2, 5, 5, 2, 32, 8]) == [2, 2, 5, 5, 8, 9, 32]

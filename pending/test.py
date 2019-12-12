def insert(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while k >= 0 and arr[j] > k:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k


if __name__ == '__main__':
    l = [1, 3, 2, 8, 5, 5]
    insert(l)
    print(l)

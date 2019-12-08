# merge sort 不是原地排序 但是时间复杂度为nlogn
# 归并排序是一个稳定的排序算法。
# 空间复杂度为O(n)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                # arr 在切片时进行了第一层的深拷贝,所以正好是一个大小为len(L) + len(R)的数组,
                # 也是因为这个原因,导致空间复杂度比较高 : O(n)
                # 虽然是稳定的nlogn排序,但是并没有快排用的多
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


import pysnooper


# @pysnooper.snoop()
def partition(arr, low, high):
    i = low  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than the pivot
        # i equals to every element which is smaller than the pivot
        # 1 为什么是arr[j]不是arr[i],因为遍历的就是j
        # 大于还是小于 :因为要把小于pivot的值都移到左边
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            # increment index of smaller element
            i = i + 1

    # 2 arr[i]永远指向排序好的后面一个元素
    # 会不会超出范围? 即使每个元素都小于了pivot,i都加一了,导致i == j,最后一次比较的时候也是自己比自己,arr[i+1]就是pivot,不会小于
    # 如果是这种极端情况,最后一行也只是pivot跟自己交换,永远不会超出index
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now
        # at right place
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':

    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i], end=' '),

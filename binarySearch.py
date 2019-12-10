# iterative search
def binarySearch(arr,n,k):
    low = 0
    high = n-1
    while low <=high:
        mid = low +(high - low)>>1
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid +1 
        else:
            high = mid - 1
    return -1
# recursive search
def binarySearch(arr,l,r,k):
    if l>r:
        return -1

    mid = l+(r-l)//2
    if arr[mid] == k:
        return mid

    if arr[mid] <k:
        return binarySearch(arr,mid+1,r,k)
    else:
        return binarySearch(arr,l,mid-1,k)


# arr = [ 2, 3, 4, 10, 40 ] 
# x = 10
  
# # Function call 
# result = binarySearch(arr, 0, len(arr)-1, x) 

# print('result',result)


# 变种问题
# 查找第一个大于等于value的值
def bSearch(arr,n, value):
    low = 0
    high = n-1
    while low <=high:
        mid = low + (high - low) >> 1
        if arr[mid]>=value:
            if mid == 0 or arr[mid-1]<value:
                return mid
            else:
                high = mid -1 

        else:
            log = mid +1 
    return -1


# 查找最后一个小于等于给定值的元素
def binarySearch(arr, n, value):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) >> 1
        if arr[mid]<=value:
            if mid == n - 1 or arr[mid + 1] >=value:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


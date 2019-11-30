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


arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 

print('result',result)
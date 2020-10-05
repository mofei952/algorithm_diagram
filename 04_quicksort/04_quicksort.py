def quicksort(array):
    if len(array) < 2:
    	return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def partition(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    return low
        
def quicksort2(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quicksort2(arr, 0, index-1)
        quicksort2(arr, index+1, high)
    return arr
        

print(quicksort([10, 5, 2, 3]))
print(quicksort2([10, 5, 2, 3], 0, 3))
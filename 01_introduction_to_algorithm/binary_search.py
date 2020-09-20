def binary_search(list, item):
    low, high = 0, len(list)-1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if item == guess:
            return mid
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

def loop_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def recursive_sum(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum(arr[1:])

print(loop_sum([1, 2, 3, 4]))
print(recursive_sum([1, 2, 3, 4]))
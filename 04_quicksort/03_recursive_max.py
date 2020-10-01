def max(arr):
    if not arr:
        return None
    if len(arr) == 1:
        return arr[0]
    value = max(arr[1:])
    return arr[0] if arr[0] > value else value

print(max([1, 2, 3, 4]))
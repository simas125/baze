def count(arr, x):
    if len(arr) == 0:
        return 0
    if arr[0] == x:
        return 1 + count(arr[1:], x)
    return count(arr[1:], x)
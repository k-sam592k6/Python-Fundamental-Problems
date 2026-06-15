def binary_search(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, right)


arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter target: "))

result = binary_search(arr, target, 0, len(arr) - 1)

print(result)

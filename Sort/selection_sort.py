def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        index = i
        min = arr[i]
        for j in range(i + 1, len(arr)):
            if min > arr[j]:
                min = arr[j]
                index = j
        t = arr[i]
        arr[i] = min
        arr[index] = t
    return arr


if __name__ == '__main__':
    print('Selection sort')
    arr = [1, 2, 3, 4, 1, 2, 1, -31, 7]
    print(arr)
    arr = selection_sort(arr)
    print(arr)

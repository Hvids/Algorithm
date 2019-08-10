def insertion_sory(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
    return arr


def _insertion_sory(arr):
    for j in range(len(arr) - 2, -1, -1):
        key = arr[j]
        i = j + 1
        while i < len(arr) and arr[i] >= key:
            arr[i - 1] = arr[i]
            i = i + 1
        arr[i - 1] = key
    return arr


if __name__ == '__main__':
    print('Insertion sort')
    arr = [1, 23, 4, 1, 2, 3, 45]
    print(arr)
    arr = _insertion_sory(arr)
    print(arr)

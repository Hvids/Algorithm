def merge(arr_left, arr_rigth):
    new_arr = []
    j = 0
    i = 0
    arr_left.append(float('+inf'))
    arr_rigth.append(float('+inf'))
    while i < len(arr_left) - 1:
        if arr_left[i] < arr_rigth[j]:
            new_arr.append(arr_left[i])
            i = i + 1
        else:
            new_arr.append(arr_rigth[j])
            j = j + 1
    new_arr = new_arr + arr_rigth[j:-1]
    return new_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    arr = merge_sort(arr[0:len(arr) // 2]) + merge_sort(arr[len(arr) // 2:])
    arr = merge(arr[0:len(arr) // 2], arr[len(arr) // 2:])
    return arr


if __name__ == '__main__':
    print('Merge sort')
    arr = [1, 4, 2, 1, 2, 34]
    print(arr)
    arr = merge_sort(arr)
    print(arr)

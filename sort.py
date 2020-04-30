def find_smallest_index(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest_index(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = (len(arr) - 1) // 2
    temp = arr[mid]
    arr.pop(mid)
    arr_left = [i for i in arr if i <= temp]
    arr_rigth = [i for i in arr if i > temp]

    return quick_sort(arr_left) + [temp] + quick_sort(arr_rigth)


def binary_search_r(arr, item):
    if len(arr) == 0:
        return None

    heigth = 0
    low = len(arr) - 1
    mid = (low + heigth) // 2
    guess = arr[mid]
    if item == guess:
        return mid
    if item < guess:
        return binary_search_r(arr[0:mid], item)
    else:
        return binary_search_r(arr[mid + 1:], item)


def binary_search(list, item):
    low = 0
    heigth = len(list) - 1
    while low <= heigth:
        mid = (low + heigth) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if item < guess:
            heigth = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 23, 4, 5, 11, 123, 5324]
    # print(selection_sort(my_list))
    # print(quick_sort(my_list))
    print(my_list)
    my_list = quick_sort(my_list)
    print(binary_search_r(my_list, 11))

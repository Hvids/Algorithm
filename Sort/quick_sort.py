import random


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i = i + 1
            t = array[i]
            array[i] = array[j]
            array[j] = t
    t = array[i + 1]
    array[i + 1] = array[r]
    array[r] = t
    return (i + 1, array)


def randomized_partition(array, p, r):
    i = int(random.uniform(p, r))
    t = array[r]
    array[r] = array[i]
    array[i] = t
    return partition(array, p, r)


def _quick_sort(array, p, r):
    if p < r:
        (q, array) = randomized_partition(array, p, r)
        array = _quick_sort(array, p, q - 1)
        array = _quick_sort(array, q + 1, r)
    return array


def quick_sort(array):
    array = _quick_sort(array, 0, len(array) - 1)
    return array


if __name__ == '__main__':
    array = [1, 2, 3, 1, 123, -1, -10, 13]
    print(array)
    array = quick_sort(array)
    print(array)

def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    max_left = -1
    for i in range(mid, low, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    rigth_sum = float('-inf')
    sum = 0
    max_rigth = -1
    for j in range(mid + 1, high):
        sum = sum + arr[j]
        if sum > rigth_sum:
            rigth_sum = sum
            max_rigth = j
    return (max_left, max_rigth, left_sum + rigth_sum)


def find_maximum_subaray(arr, low, high):
    if high == low:
        return(low, high, arr[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = find_maximum_subaray(arr, low, mid)
        (rigth_low, rigth_high, rigth_sum) = find_maximum_subaray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(
            arr, low, mid, high)
        if left_sum >= rigth_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif rigth_sum >= left_sum and rigth_sum >= cross_sum:
            return (rigth_low, rigth_high, rigth_sum)
        else:
            return(cross_low, cross_high, cross_sum)


if __name__ == '__main__':
    print('Find maximum subarray')
    arr = [-1, 2, 34, -5]
    print(arr)
    print(find_maximum_subaray(arr, 0, len(arr)-1))

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

def randomized_select(array,p,r,i):
    if p == r:
        return array[p]
    (q,array) = randomized_partition(array,p,r)
    k = q-p+1
    if i == k:
        return array[q]
    elif i < k:
        return randomized_select(array,p,q-1,i)
    else:
        return randomized_select(array,q+1,r,i-k)

if __name__ == '__main__':
    array = [12,3,5,4,12,3,12]
    print(array)
    print(randomized_select(array,0,len(array)-1,5))

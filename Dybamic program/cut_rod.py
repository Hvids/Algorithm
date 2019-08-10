def bottomUpCutRod(p):
    n = len(p)
    r = [float('-inf')]*n
    r[0] = 0
    for j in range(1, n ):
        q = float('-inf')
        for i in range(1,j + 1):
            q = max(q,p[i] + r[j-i])
        r[j] = q
    return r[n - 1]

if __name__ == '__main__':
    p = [1,2,3,4]
    print(bottomUpCutRod(p))

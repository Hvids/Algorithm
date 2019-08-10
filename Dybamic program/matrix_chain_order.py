def matrix_chain_order(p):
    n = len(p) - 1
    m = []
    for i in range(n):
        m.append([0]*n)
    s = []
    for i in range(n):
        s.append([None]*n)
    for l in range(1, n):
        for i in range(1,n-l+1):
            j = i + l -1

            m[i][j] = float('inf')
            for k in range(i,j-1):
                q = m[i,k] + m[k+1,j] + p[i-1]*p[k][j]
                if q < m[i,j]:
                    m[i,j] = q
                    s[i,j] = k
    return (m,s)
def print_optimal_parens(s,i,j):
    if i == j:
        print("A")
    else:
        print('(')
        print_optimal_parens(s,i,s[i,j])
        print_optimal_parens(s,s[i,j]+1,j)
        print(')')

if __name__ == '__main__':
    p = [1,2,3,1]
    (m,s) = matrix_chain_order(p)
    print_optimal_parens(s,0,0)

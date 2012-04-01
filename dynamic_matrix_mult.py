# NOTE: This is not yet working properly. Likely some sort of off-by-one logic
# error.
# See CLRS p376 (pdf p397) for the correct answer.
def matrix_chain_order(p):
    """ 'p' is a lst containing sizes which are used to determine the
    dimensions of each array. An array has dimension p_i x p_(i+1).
    Runtime: n^3.
    Storage: n^2."""
    n = len(p) - 1

    s = [[-float("inf") for i in range(n)] for i in range(n)]
    m = [[float("inf") for i in range(n)] for i in range(n)]
    for i in range(n):
        m[i][i] = 0
    for l in range(2, n+1): # length of chain
        for i in range(n-l+1):
            j = i + l - 1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                print l, "|", i, k, "|", k+1, j, "|", p[i-1]*p[k]*p[j], "|", q
                #print k, q, m[i][j], i, j
                if q < m[i][j]:
                    s[i][j] = k
                    m[i][j] = q
    return s, m
    
s, m = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])
print "s:", s
print "m:", m

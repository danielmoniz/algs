def cut_rod(prices, n):
    if n == 0:
        return 0
    q = -float("inf")
    for i in range(1, n+1):
        q = max(q, prices[i] + cut_rod(prices, n-i))
    return q

def memoized_cut_rod_aux(prices, n, r):
    if r[n] >= 0:
        return r[n]

    q = -float("inf")
    for i in range(1, n+1):
        q = max(q, prices[i] + memoized_cut_rod_aux(prices, n-i, r))
    r[n] = q
    return q

def memoized_cut_rod(prices, n):
    r = [-float("inf") for i in range(0, n+1)]
    r[0] = 0
    return memoized_cut_rod_aux(prices, n, r)
    

def bottum_up_cut_rod(prices, n):
    r = [0]
    for i in range(1, n+1):
        q = -float("inf")
        for j in range(1, i+1):
            q = max(q, prices[j] + r[i-j])
        r.append(q)
    return r[n], r

def extended_bottum_up_cut_rod(prices, n):
    r = [0]
    s = [0 for i in range(n+1)]
    for i in range(1, n+1):
        q = -float("inf")
        for j in range(1, i+1):
            if q < prices[i] + r[i-j]:
                q = prices[j] + r[i-j]
                s[i] = j
        r.append(q)
    return s, r

def print_rod_cut_solution(prices, n):
    s, r = extended_bottum_up_cut_rod(prices, n)
    while n > 0:
        print s[n]
        n = n - s[n]
    


    
    

n = 12 # length of rod
prices = [0, 1, 5, 8, 9, 10, 17, 20, 24, 30, 30, 30, 30]
#print cut_rod(prices, 4)

#print memoized_cut_rod(prices, n)
#print bottum_up_cut_rod(prices, n)
#print extended_bottum_up_cut_rod(prices, n)
print_rod_cut_solution(prices, n)

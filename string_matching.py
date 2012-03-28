def naive_string_matcher(text, pattern):
    n = len(text)
    m = len(pattern)
    for s in range(n - m + 1):
        if pattern == text[s : s+m]:
            print "Pattern occurs with shift", s - 1

def rabin_karp_matcher(text, pattern, d, q):
    """d is the number of digits in the alphabet (radix-d digits). q will be
    the modulus that ensures the numbers we are working with are reasonbly
    small."""
    n = len(text)
    m = len(pattern)
    print "n:", n, ", m:", m
    h = (d**(m - 1)) % q
    p = 0
    t = []
    t.append(0)
# preprocessing
    for i in range(m):
        p = (d*p + int(pattern[i])) % q
        t[0] = (d*t[0] + int(text[i])) % q

# matching
    for s in range(n - m + 1):
        print t, "index:", s
        if p == t[s]:
            if pattern == text[s : s + m]:
                print "Pattern occurs with shift", s
        if s < n - m:
            new_t_value = (d*(t[s] - int(text[s]) * h) + int(text[s + m])) % q
            t.append(new_t_value)
            

#naive_string_matcher("oogly boogly goog", "oog")
rabin_karp_matcher("1449314322375314", "14", 10, 13)

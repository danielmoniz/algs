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
    spurious_hits = 0
    for s in range(n - m + 1):
        #print t, "index:", s
        if p == t[s]:
            if pattern == text[s : s + m]:
                print "Pattern occurs with shift", s
            else:
                spurious_hits += 1
        if s < n - m:
            new_t_value = (d*(t[s] - int(text[s]) * h) + int(text[s + m])) % q
            t.append(new_t_value)
    print "Spurious hits:", spurious_hits

def finite_automaton_matcher(text, delta, m):
    """'text' is the text upon which to search for a match. 'delta' is the
    finite automaton generated from the pattern we want to find. 'm' is the
    accepted state for the automaton."""
    n = len(text)
    q = 0
    for i in range(n):
        q = delta(q, text[i])
        if q == m:
            print "Pattern occurs with shift", i-m
            
def get_string_matching_automaton(pattern, alphabet):
    """Pattern is the pattern around which we want to create this finite
    automaton. Alphabet is the available alphabet for the string we'll be
    matching on."""
    m = len(pattern)
    automaton_array = []
    for q in range(m+2):
        automaton_array.append({})
        for char in alphabet:
            k = min(m, q+1)
            while not (pattern[:q] + char).endswith(pattern[:k]):
                k -= 1
            automaton_array[q][char] = k
    print "automaton_array:", automaton_array
    return lambda x,y: automaton_array[x][y]

# Knuth-Morris-Pratt matching algorithm
# runtime of O(n)
def kmp_matcher(text, pattern):
    print "--------------------------"
    print "text:", text
    print "pattern:", pattern
    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    print "--------------------------"
# q stores the number of characters matched
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q-1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == m:
            print "Pattern occurs with shift", i - m
            q = pi[q-1] # look for the next match

# preprocessing of O(m)
def compute_prefix_function(pattern):
    m = len(pattern)
    pi = []
    pi.append(0)
    k = 0
    for q in range (1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k]
        if pattern[k] == pattern[q]:
            k = k + 1
        pi.append(k)
    print "prefix function:", pi
    return pi


pattern = "ababaca"
#prefix_function = compute_prefix_function(pattern)
kmp_matcher("bacbabababacababacab", pattern)

#naive_string_matcher("oogly boogly goog", "oog")

#rabin_karp_matcher("3141592653589793", "26", 10, 11)

#delta = get_string_matching_automaton("aabab", "ab")
#finite_automaton_matcher("aabaabaababaabb", delta, len("aabab"))

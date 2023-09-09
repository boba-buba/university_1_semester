import math
def swap(cisla, i, j):
    cisla[i], cisla[j] = cisla[j], cisla[i]
    return
def reverse(cisla, start):
    i = start; j = len(cisla) -1
    while i < j:
        cisla[i], cisla[j] = cisla[j], cisla[i]
        i += 1
        j -= 1
    return
def next_permutace(cisla):
    i = len(cisla) -2
    while i >= 0 and cisla[i+1] <= cisla[i]:
        i -= 1
    if i >= 0:
        j = len(cisla) - 1
        while cisla[j] <= cisla[i]:
            j -= 1
        cisla[i], cisla[j] = cisla[j], cisla[i]
    reverse(cisla, i+1)
ls = [1, 2, 3, 4, 5]
def perm(k, m, n):
    print(k, m, n)
    if n == 0:
        print(m)
        return
    b = (k//(math.factorial(n-1)))
    print(ls[b])
    m.pop(m.index(b))
    #m = m.sort()

    #print(m)
    return perm(k%(math.factorial(n-1)), m, n-1)

def ithPermutation(n, i):
    j = 0; k = 0
    fact = [1 for i in range(n)]
    permut = [1 for i in range(n)]
    fact[0] = 1
    k = 1
    while k < n:
        fact[k] = fact[k-1] * k
        k+=1
    for k in range(n):
        permut[k] = i // fact[n-1-k]
        i = i % fact[n-1-k]
    for k in range(n-1, 0, -1):
        for j in range(k-1, -1, -1):
            if (permut[j] <= permut[k]):
                permut[k] += 1

    return permut
    #for k in range(n):
    #    print(permut[k]+1, end=' ')
    #print()
k = 0
p = []

pocet, misto = map(int, input().split())
per = list(map(int, input().split()))

if misto < 0:
    misto = math.factorial(pocet) + misto
perMap = ithPermutation(pocet, misto)
print(perMap)

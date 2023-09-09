
def joseph3(n):
    if n <= 0:
        return 'ERROR'
    res = 0
    k = 2
    for i in range(1, n+1):
        res = (res + k) % i
    return res + 1
#print(joseph3(pocet))

def proverka(pole, m, n, znak):
    for i in range(len(pole[0])):
        count = 0
        for j in range(i, len(pole[0])):
            if pole[m][j] == znak:
                count += 1
                if count == 5: return False
    for i in range(len(pole)):
        count = 0
        for j in range(i, len(pole)):
            if pole[j][n] == znak:
                count += 1
                if count == 5: return False

    delka = min(len(pole[0]), len(pole))
    for i in range(delka):
        count = 0
        for j in range(i, delka):
            if pole[i][i] == znak:
                count += 1
                if count == 5: return False

    count = 0
    i = m - 1; j = n + 1
    while i >= 0 and j < n:
        if pole[i][j] == znak:
            count+=1
            if count == 5: return False
        i -= 1; j += 1
    return True

def remize(r,s):
    deska = [[ "_" for l in range(s)] for k in range(r)]
    i = 0; j = 0
    for i in range(r):
        for j in range(s):
            deska[i][j] = "O"
            if not proverka(deska, i, j, "O"):
                deska[i][j] = "X"

    return deska
radky, sloupce = map(int, input().split())

d = remize(radky, sloupce)
for i in range(radky):
    for j in range(sloupce):
        print(d[i][j], end='')
    print()
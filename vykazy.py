def platnost(s):
    if len(s) >= 5 and s[0] == s[-2]:
        return True

def prevod_sek(cas):
    cas = cas.split(':')
    sekundy = 3600 * int(cas[0]) + 60 * int(cas[1]) + int(cas[2])
    return sekundy
def prevod_z_sek(cas):
    hodiny = cas//3600
    minuty = (cas % 3600) // 60
    sekundy = cas % 60
    minuty = str(minuty//10) + str(minuty%10)
    sekundy = str(sekundy//10) + str(sekundy%10)

    return f'{hodiny}:{minuty}:{sekundy}'

lines = []
while True:
    line = input()
    if line != '.':
        lines.append(line.split())
    else:
        break
aktivity = {}

for i in lines:
    if platnost(i):
        aktivita = i[2:-2]
        a = ""
        for k in aktivita:
            a = a + k + " "
        if a not in aktivity:
            aktivity[a] = 0
            maximum = a



celkem = 0
for i in aktivity:
    for j in lines:
        if platnost(j):
            konkretnaja_akt = j[2:-2]
            a = ""
            for k in konkretnaja_akt:
                a = a + k + " "
            if a == i:
                aktivity[i] += prevod_sek(j[-1]) - prevod_sek(j[1])
    celkem += aktivity[i]
aktivity.items()

delky = []
for j in aktivity:
    delky.append(aktivity[j])
delky.sort()
delky = delky[::-1]

for i in delky:
    for j in aktivity:
        if aktivity[j] == i:
            print(f'{prevod_z_sek(aktivity[j])} {j[:-1]}')

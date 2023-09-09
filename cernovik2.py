def joseph(n, k):
    if n == 1: return 1
    return (joseph(n - 1, k) + k - 1) % n + 1

pocet = int(input())
def joseph2(person, k, index):
    if len(person) == 1:
        print(person[0])
        return
    index = (index+k)%len(person)
    person.pop(index)
    joseph2(person, k, index)

person = []
for i in range(1, pocet +1): person.append(i)
k = 2
k-=1
#joseph2(person, k, 0)
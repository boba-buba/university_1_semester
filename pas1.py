import random
import numpy
import matplotlib.pyplot as plt

arrayX = []
def generating_rv():
    number = 1_000_000
    suma = 0
    count04 = 0
    suma_prevr = 0
    count23 = 0
    count23_ = 0

    for i in range(0, number):
        temp = random.random()
        suma += temp
        temp_prevr = 1 / temp
        arrayX.append(temp_prevr)
        suma_prevr += temp_prevr
        if temp < 0.4:
            count04 += 1
        if 3 >= temp_prevr >= 2:
            if 3 > temp_prevr > 2:
                count23_ += 1
            count23 += 1
    shY = suma / number
    shX = suma_prevr / number
    p04 = count04/number * 100
    p23 = count23 / number * 100
    p23_ = count23_ / number * 100
    print(shY, shX, p04, p23, p23_)

generating_rv()

a = numpy.array(arrayX)
print(numpy.histogram(a))
fig, ax = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
ax.hist(a, bins = range(0, 20))
plt.show()

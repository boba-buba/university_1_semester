import random
sum = 0
count_experiments = 1_000_000
expected_val = 0

for i in range(0, count_experiments):
    a = random.randrange(1, 7)
    sum += a
    #print("0. roll ", a)
    count_rolls_after_6 = 0
    while a == 6:
        a = random.randrange(1, 7)
        sum += a
        count_rolls_after_6 += 1
        #print("previous roll was 6, and this is", count_1, ". roll and now it is ", a)
expected_val = sum / count_experiments

print(expected_val, sum)
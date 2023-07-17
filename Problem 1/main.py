# A person is
# Gene, time
# Gene between 0 and 1, called g
# At the end of each step, prob g*g to reproduce, 2*g*(1-g) to survive, (1-g)(1-g) to die
import random


def prob(p):
    return [int(p * 1000000), 1000000]


def bernoulli(p):
    p = prob(p)
    k = random.randint(1, 1000000)
    return k <= p[0]


lst = [(0.2, 0)] * 100
lst1 = [0.5]
for t in range(10000):

    dead = []
    new = []
    i = 0
    for a, b in lst:
        if b > 3:
            dead.append(i)
            continue
        p1 = a * a
        if bernoulli(p1):
            k = random.randint(0, 1)
            if k == 0:
                a1 = max(0, a - 0.000005)
            else:
                a1 = min(1, a + 0.000001)
            new.append((a1, 0))
            continue
        if bernoulli(((a - 1) ** 2) / (1 - a * a)):
            dead.append(i)
            continue
        i += 1
    for i in dead[::-1]:
        lst = lst[:i] + lst[i + 1:]
        lst1 = lst1[:i] + lst1[i + 1:]
    for i in new:
        lst.append(i)
        lst1.append(i[0])
    lst.sort()
    lst1.sort()
    if len(lst1) > 10000:
        lst = lst[len(lst) - 100000:]
        lst1 = lst1[len(lst1) - 100000:]
    # print(lst)
    print(sum(lst1) / max(len(lst), 1))
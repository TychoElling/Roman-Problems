import math
import random


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Note: We are not using sqrt because we only care about 1

class Circles:
    def __init__(self, C, T):
        self.C = C
        self.T = T
        self.points = [(0, 0, 0, None, 0)]  # a point is (n,x,y,p,t)\
        self.N = 1

    def validPoint(self, c):
        for n, x, y, p, t in self.points:
            if distance(x, y, c[1], c[2]) < 1:
                return False
        return True

    def findPoint(self, c, count=0):
        if count > 900:
            return None
        theta = random.uniform(0, 2 * math.pi)
        x, y = math.cos(theta) + c[1], math.sin(theta) + c[2]
        if self.validPoint(("", x, y, "", "")):
            self.N += 1
            return (self.N - 1, x, y, c[0], 0)
        return self.findPoint(c, count + 1)

    def step(self):
        dead = []
        i = 0
        for n, x, y, p, t in self.points:
            if t == self.T:
                dead.append(i)
            i += 1
        for i in dead[::-1]:
            self.points = self.points[:i] + self.points[i + 1:]
        new = []
        for n, x, y, p, t in self.points:
            c = (n, x, y, p, t)
            if t != 0:
                continue
            lst = [self.findPoint(c) for i in range(self.C)]
            for i in lst:
                if i != None:
                    new.append(i)
        self.points = [(n, x, y, p, t + 1) for n, x, y, p, t in self.points]
        self.points += new

    def components(self):
        points = self.points.copy()
        points = sorted(points)[::-1]
        k = max([i[4] for i in points])
        c = 0
        for n,x,y,p,t in points:
            if t == k:
                c += 1
        return c

    def simulate(self, iterations=10):
        for i in range(iterations):
            self.step()
            #print("iteration:",i+1,population:",len(self.points),"components:",self.components())

f = open("circleComponents.txt","w")
for i in range(100):
    s = Circles(2,1)
    s.simulate(7)
    print(len(s.points), s.components(), file=f)
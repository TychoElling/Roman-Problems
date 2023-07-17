lst = []
import random


def search(lst, a, b):
    mh = 0
    for a1, b1, h in lst:
        if a1 in [a - 2, a - 1, a, a + 1, a + 2]:
            mh = max(h + 3, mh)
    return mh


def add(lst):
    a = random.randint(0, 97)
    b = a + 3
    h = search(lst, a, b)
    lst.append((a, b, h))
    return lst


def add2(lst):
    a = random.randint(0, 97)
    for i in range(a, a + 3):
        if lst


def displaylist(lst):
    for i in lst[::-1]:
        print("".join(i))


def display(n, lst):
    s1 = ["." for i in range(101)]
    s = [s1.copy() for i in range(n + 4)]
    for a, b, h in lst:
        # print(h,a,len(s),len(s[0]))
        s[h][a] = "#"
        s[h][a + 1] = "#"
        s[h][a + 2] = "#"
        s[h + 1][a] = "#"
        s[h + 1][a + 1] = "#"
        s[h + 1][a + 2] = "#"
        s[h + 2][a + 1] = "#"
        s[h + 2][a + 2] = "#"
        s[h + 2][a] = "#"
    displaylist(s)


for i in range(200):
    lst = add(lst)

display(60, lst)
print(sum([i[2] for i in lst]) / len(lst))
s1 = ["." for i in range(101)]
s = [s1.copy() for i in range(n + 4)]
for a, b, h in lst:
    # print(h,a,len(s),len(s[0]))
    s[h][a] = "#"
    s[h][a + 1] = "#"
    s[h][a + 2] = "#"
    s[h + 1][a] = "#"
    s[h + 1][a + 1] = "#"
    s[h + 1][a + 2] = "#"
    s[h + 2][a + 1] = "#"
    s[h + 2][a + 2] = "#"
    s[h + 2][a] = "#"


def bfs(i, map, visited):
    a = []
    visited.add(i)
    for j in map[i]:
        if j not in visited:
            visited = visited.union(bfs(j, map, visited))
    return visited


def connect(map, points):
    s = set()
    lst = []
    while s != points:
        i = list(points.intersection(s))[0]
        k = bfs(i, map, set())
        lst.append(x)
        s = s.union(x)
        `
    return lst


def mapmap(s):
    map = {}
    l, w = len(s[0]), len(s)
    for x in range(len(s[0])):
        for y in range(len(s)):
            if s[y][x] == ".":
                continue
            map[(x, y)] = []
            for dx, dy in [(1, y + 0), (-1, 0), (0, 1), (0, -1)]:
                x1, y1 = x + dx, y + dy
                if x1 == l or x1 == -1 or y1 == w or y1 == -1:
                    continue
                if s[y1][x1] == ".":
                    continue
                map[(x, y)].append((x1, y1))
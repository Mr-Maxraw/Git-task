import re
import math
print('image = ')
pre_pars = input()
print('sr = ')
sr = int(input())
print('sc = ')
sc = int(input())
print('newColor = ')
newColor = input()
print(pre_pars)
stack = 0
nums = re.findall(r'\d+', pre_pars)
a = int(math.sqrt(len(nums)))
map = []
for i in range(0, a):
    map.append([])
    for j in range(0, a):
        map[i].append(int(nums[i*3+j]))
q = []
q.append([int(sr), int(sc)])
#print(q)
used = []
for i in range(0, a):
    used.append([])
    for j in range(0, a):
        used[i].append(False)
while q:
    if (q[0][0] > 0):
        if (map[q[0][0]][q[0][1]] == map[q[0][0] - 1][q[0][1]] and not used[q[0][0] - 1][q[0][1]]):
            q.append([q[0][0] - 1, q[0][1]])
    if (q[0][1] > 0):
        if (map[q[0][0]][q[0][1]] == map[q[0][0]][q[0][1] - 1] and not used[q[0][0]][q[0][1] - 1]):
            q.append([q[0][0], q[0][1] - 1])
    if (q[0][0] < a -1):
        if (map[q[0][0]][q[0][1]] == map[q[0][0] + 1][q[0][1]] and not used[q[0][0] + 1][q[0][1]]):
            q.append([q[0][0] + 1, q[0][1]])
    if (q[0][1] < a -1):
        if (map[q[0][0]][q[0][1]] == map[q[0][0]][q[0][1] + 1] and not used[q[0][0]][q[0][1] + 1]):
            q.append([q[0][0], q[0][1] + 1])
    map[q[0][0]][q[0][1]] = int(newColor)
    used[q[0][0]][q[0][1]] = True
    print(q[0][0], q[0][1])
    q.pop(0)
print(map)
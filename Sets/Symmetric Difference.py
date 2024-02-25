from collections import OrderedDict

n = input()
a = input()
list1 = list(OrderedDict.fromkeys(map(int, a.split())))

n = input()
b = input()
list2 = list(OrderedDict.fromkeys(map(int, b.split())))

res = list(set(list1).difference(set(list2)))
res += list(set(list2).difference(set(list1)))
res.sort()

for i in res:
    print(i)

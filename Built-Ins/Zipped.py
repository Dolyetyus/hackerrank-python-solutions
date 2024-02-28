n = list(map(int, input().split()))

a = list(map(float, input().split()))

for _ in range(n[1]-1):
    b = list(map(float, input().split()))
    a += b

res = list(zip(*[iter(a)]*n[0]))
 
for i in zip(*res):
    print(sum(i)/len(i))

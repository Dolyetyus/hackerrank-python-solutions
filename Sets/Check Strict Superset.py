s1 = set(map(int, input().split()))

n = int(input())
cout = True

for _ in range(n):
    s2 = set(map(int, input().split()))
    
    if not (set(s2) <= set(s1)):
        cout = False
        break
    
print(cout)

cases = int(input())

for _ in range(cases):
    n = int(input())
    s1 = set(map(int, input().split()))

    n = int(input())
    s2 = set(map(int, input().split()))
    
    print(set(s1) <= set(s2))

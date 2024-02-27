n = int(input())
s = set(map(int, input().split()))

orders = int(input())

for _ in range(orders):
    command = input()
    set2 = set(map(int, input().split()))
    
    if command[:6]=="update":
        s.update(set2)
    elif command[:19]=="intersection_update":
        s.intersection_update(set2)
    elif command[:27]=="symmetric_difference_update":
        s.symmetric_difference_update(set2)
    elif command[:17]=="difference_update":
        s.difference_update(set2)
        
print(sum(s))

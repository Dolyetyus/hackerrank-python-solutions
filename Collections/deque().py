from collections import deque

d = deque()

num_orders = int(input())

for _ in range(num_orders):
    command = input()
    
    if command=="pop":
        d.pop()
    elif command=="popleft":
        d.popleft()
    elif command[:10]=="appendleft":
        d.appendleft(int(command[11:]))
    elif command[:6]=="append":
        d.append(int(command[7:]))

print(" ".join(map(str, d)))

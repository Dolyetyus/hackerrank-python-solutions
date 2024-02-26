n = int(input())
s = set(map(int, input().split()))

num_orders = int(input())

for _ in range(num_orders):
    command = input()
    
    if command=="pop":
        s.pop()
    elif command[:6]=="remove":
        num = int(command[7:])
        if num in s:
            s.remove(num)
    elif command[:7]=="discard":
        num = int(command[8:])
        if num in s:
            s.discard(num)

print(sum(s))


from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
m = int(input())

shoe_inventory = Counter(shoe_sizes)
ret = 0

while m>0:
    size, price = map(int, input().split())
    m-=1
    if shoe_inventory[size] > 0:
        ret += price
        shoe_inventory[size] -= 1

print(ret)

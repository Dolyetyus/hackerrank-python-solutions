a = input()
li = list(map(int, input().split()))

print("True") if all([i >= 0 for i in li]) and any([str(i)[0] == str(i)[-1] for i in li]) else print("False")

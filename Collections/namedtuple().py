from collections import namedtuple

total = 0
n = int(input())
columns = namedtuple("Student", input())

for i in range(n):
    st = input().split()
    student = columns(*st)
    total += int(student.MARKS)
    
print("%.2f" % (total/n))

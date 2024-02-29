cube = lambda x: pow(x, 3)

def fibonacci(n):
    if n==1:
        return [n-1]
    if n==0:
        return []
        
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
        
    return fib
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

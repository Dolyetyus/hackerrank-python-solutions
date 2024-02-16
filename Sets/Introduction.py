def average(array):
    thisset = set(array)
    
    return sum(thisset)/len(thisset)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

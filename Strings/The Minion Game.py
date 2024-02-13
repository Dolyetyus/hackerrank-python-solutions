vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def minion_game(string):
    n = len(string)
    kevin = 0
    stuart = 0
    
    stuart = 0
    for i in range(n):
        if s[i] in vowels:
            kevin += n-i
        else:
            stuart += n-i

    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif kevin < stuart:
        print("Stuart " + str(stuart))
    else:
        print("Draw")
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)

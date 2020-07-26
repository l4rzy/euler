def is_multiple_35(num):
    if num%3 == 0 or num%5 == 0:
        return True
    return False

def solve():
    S = 0
    for i in range(1000):
        
        if is_multiple_35(i):
            print(i)
            S += i
    print(S)
    
solve()
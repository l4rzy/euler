LIMIT = 4000000

def solve():
    S = 0
    m = 1
    n = 2
    while n < LIMIT and m < LIMIT:
        if n %2 == 0:
            print(f'n = {n}')
            S += n 
        if m %2 == 0:
            print(f'm = {m}')
            S += m
        m = m+n
        n = m+n
    print(S)
    
solve()
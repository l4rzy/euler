# solve the hard way :D
def check(cf, df):
    mcf = {i: cf.count(i) for i in cf}
    mdf = {i: df.count(i) for i in df}
    r = {}
    for k in mdf:
        if k not in mcf:
            r[k] = mdf[k]
        else:
            if mcf[k] < mdf[k]:
                r[k] = mdf[k] - mcf[k]
    return r
    
def primes(n):
    print(f'factorization of {n} is ', end = '')
    facs = []
    d  = 2 
    while d**2 <= n:
        while n%d == 0:
            facs.append(d)
            n = n//d
        d+=1
        
    if n > 1:
        facs.append(n)
    print(f'{facs}')
    return facs

def solve(limit):
    cf = [] # current factorials    
    for i in range(2,limit+1):
        df = primes(i) # divisor factorials
        r = check(cf, df)
        print(r)
        
        for k in r:
            for x in range(r[k]):
                cf.append(k)
    
    print(cf)
    N = 1
    for i in cf:
        N *= i
        
    print(N)
solve(20)
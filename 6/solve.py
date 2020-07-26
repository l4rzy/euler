def sum_of_squares(n):
    S = 0
    for i in range(1,n+1):
        S += i**2
    return S
    
    
def square_of_sum(n):
    S = 0
    for i in range(1, n+1):
        S += i
    return S**2
    
print(f'result = {square_of_sum(100)-sum_of_squares(100)}')
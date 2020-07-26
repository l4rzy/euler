
def check(num):
    if str(num) == str(num)[::-1]: return True
    return False

lst = []
for i in range(100, 999):
    for j in range(100, 999):
        if check(i*j) == True:
            lst.append(j*i)
            
print(max(lst))
            
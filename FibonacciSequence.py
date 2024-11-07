
def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    
    values = [t1, t2]

    for i in range(2, n+1):
        temp = values[i-2] + values[i-1] ** 2
        values.append(temp)

    return values[n-1]


print(fibonacciModified(0,1,5))
def powerSum(X, N, num=1):
    if X == 0:
        return 1
    elif X < 0:
        return 0
    count = 0
    
    while num ** N <= X:
        count += powerSum(X-num ** N, N, num+1)
        num += 1
    return count